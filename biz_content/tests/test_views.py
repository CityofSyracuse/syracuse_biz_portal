import requests_mock
import json
from . import factories
from biz_content import models, forms
from django.test import TestCase, TransactionTestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Permission
from django.utils import html
from django.conf import settings
from biz_content.views import PROJECT_SUCCESS, PROJECT_FAILURE
import os
from urllib.parse import urljoin


class UpdateCheckboxTestCase(TestCase):

    def setUp(self):
        self.user = factories.UserFactory()
        self.project = self.user.projects.all()[0]
        self.step_page = factories.StepPageFactory()
        self.url = reverse('update-checkbox', kwargs={
            'steppage_id': self.step_page.pk,
            'project_id': self.project.pk,
        })

    def test_valid_checked_item(self):
        self.client.force_login(self.user)
        item = self.step_page.checklist_items.first()
        res = self.client.post(self.url, {
            'checklist': (item.pk,),
        })
        self.assertEquals(res.status_code, 200)
        json = res.json()
        checked_items = json['checked_items']
        self.assertEquals(len(checked_items), 1)
        pk = checked_items[0]
        self.assertEquals(pk, item.pk)


class ProfileViewTestCase(TestCase):

    def setUp(self):
        """Set Up User
        Set up user with permissions to access admin."""
        self.user = factories.UserFactory()
        self.user.save()
        self.steppage = factories.StepPageFactory()
        self.steppage.save()
        self.project = self.user.projects.first()
        self.project.checklists.add(self.steppage)
        self.project_default_data = {
            'business_type': 'llc', 'dba_name': 'bakery'}
        self.project.__dict__.update(self.project_default_data)
        self.project.save()

    def test_view_redirects_to_login(self):
        """Profile redirect to login if not logged in.
        """
        res = self.client.get(reverse('profile'))
        expected_redirect = "%s?next=%s" % (
            reverse('auth_login'), reverse('profile'))

        self.assertRedirects(res, expected_redirect)

    def test_auth_user_logs_in(self):
        """User goes to profile if logged in.
        """
        self.client.force_login(self.user)
        res = self.client.get(reverse('profile'))
        self.assertEquals(res.status_code, 200)

    def test_user_can_view_project_information(self):
        self.client.force_login(self.user)
        res = self.client.get(reverse('profile'))

        for k, v in self.project_default_data.items():
            self.assertContains(res, html.conditional_escape(v))

    def test_can_user_update_project_information(self):
        self.client.force_login(self.user)
        project_updated_data = {'dba_name': 'pizzeria', 'id': self.project.id}
        res = self.client.post(
            reverse('profile'), project_updated_data, follow=True)
        self.assertEquals(res.status_code, 200)
        context = res.context
        self.assertEquals(context['projects'][0], self.project)
        self.assertEquals(context['project_id'], self.project.pk)
        messages = list(context['messages'])
        self.assertEqual(str(messages[0]), PROJECT_SUCCESS)

    def test_user_gets_error_if_invalid_information(self):
        self.client.force_login(self.user)
        bad_data_variable = 'this' * 200
        project_updated_data = {
            'dba_name': bad_data_variable, 'id': self.project.id}
        res = self.client.post(
            reverse('profile'), project_updated_data, follow=True)
        self.assertEquals(res.status_code, 200)
        context = res.context
        self.assertEquals(context['projects'][0].dba_name, 'bakery')
        self.assertEquals(context['project_id'], self.project.pk)
        messages = list(context['messages'])
        self.assertEqual(str(messages[0]), PROJECT_FAILURE)


class DashboardViewTestCase(TestCase):

    def setUp(self):
        """Set Up User
        Set up user with permissions to access admin."""

        self.user = factories.UserFactory()
        self.user.is_staff = True
        p = Permission.objects.get(codename='access_admin')
        self.user.user_permissions.add(p)
        self.user.save()

    def test_view_redirects_to_wagtail(self):
        """Test Not Login Redirects
        Not logged in user redirects to login from dashboard.
        """
        res = self.client.get(reverse('wagalytics_dashboard'))
        new_url = "%s?next=%s" % (
            reverse('wagtailadmin_login'), reverse('wagalytics_dashboard'))

        self.assertRedirects(res, new_url)

    def test_view_returns_200(self):
        """Test Logged in User Can Access
        Logged in user goes to dashboard.
        """
        self.client.force_login(self.user)
        res = self.client.get(reverse('wagalytics_dashboard'))
        self.assertEquals(res.status_code, 200)

class BusinessLicenseViewTestCase(TestCase):

    def setUp(self):
        pass

    @requests_mock.Mocker()
    def test_200_with_business_licenses(self, m):
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        application_data = open(os.path.join(__location__, 'application_data.json'), 'r')
        inspection_data = open(os.path.join(__location__,'inspection_data.json'), 'r')
        payment_data = open(os.path.join(__location__,'payment_data.json'), 'r')
        license_id = 'CU2014-0050'
        mock_urls = {"application_data":application_data,
                        "inspection_data":inspection_data,
                        "payment_data":payment_data}

        for url, data in mock_urls.items():
            relative_url = urljoin(url, license_id)
            m.get(urljoin(settings.SYRACUSE_IPS_URL, relative_url) , text=str(data))

        res = self.client.get(reverse('biz_license_status'))
        self.assertEquals(res.status_code, 200)
        context = res.context

        self.assertEquals(context['application_data'], application_data)
        self.assertEquals(context['inspection_data'], inspection_data)
        self.assertEquals(context['payment_data'], payment_data)

    @requests_mock.Mocker()
    def test_no_business_licenses(self, m):
        license_id = 'CU2014-005089403'
        mock_urls = {"application_data":[],
                        "inspection_data":[],
                        "payment_data":[]}

        for url, data in mock_urls.items():
            relative_url = urljoin(url, license_id)
            m.get(urljoin(settings.SYRACUSE_IPS_URL, relative_url) , text=str(data))

        res = self.client.get(reverse('biz_license_status'))
        self.assertEquals(res.status_code, 200)
        context = res.context
        self.assertEquals(context['messages'].value, 'Your permit could not be found. Please contact the NBD.')














