from . import factories
from biz_content import models, forms
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.http import QueryDict
from django.test import TestCase, TestCase
from django.test.client import RequestFactory


class ChecklistFormTestCase(TestCase):

    def setUp(self):
        self.user = factories.UserFactory()
        self.project = self.user.projects.all()[0]
        self.step_page = factories.StepPageFactory()

    def test_init_without_project(self):
        """Checkbox items and form items should match"""
        form = forms.ChecklistForm(self.step_page)
        cl = form.fields['checklist']
        form_qs = cl._queryset.values('pk')
        qs = self.step_page.checklist_items.values('pk')
        self.assertQuerysetEqual(qs, form_qs, transform=lambda x: x)

    def test_init_with_project(self):
        form = forms.ChecklistForm(self.step_page, project=self.project)
        cl = form.fields['checklist']
        form_qs = cl._queryset.values('pk')
        qs = self.step_page.checklist_items.values('pk')
        self.assertQuerysetEqual(qs, form_qs, transform=lambda x: x)
        model_items = self.project.checked_items.values('pk')
        form_items = cl.initial
        self.assertQuerysetEqual(model_items, form_items,
                                 transform=lambda x: x)

    def test_add_checklist_without_checked_items(self):
        rf = RequestFactory()
        request = rf.post('/', {})
        request.user = self.user
        request._dont_enforce_csrf_check = False
        form = forms.ChecklistForm(self.step_page, request.POST,
                                   project=self.project)
        self.assertTrue(form.is_valid())
        form.save()
        self.assertEqual(self.project.checklists.count(), 1)

    def test_cleaned_data(self):
        rf = RequestFactory()
        items = self.step_page.checklist_items.all()
        query = {'checklist': tuple(items.values_list('pk', flat=True))}
        request = rf.post('/', query)
        request.user = self.user
        request._dont_enforce_csrf_check = False
        form = forms.ChecklistForm(self.step_page, request.POST,
                                   project=self.project)
        self.assertTrue(form.is_valid())
        checked_items = form.cleaned_data['checklist']
        self.assertEquals(checked_items.count(), items.count())

    def test_add_checklist_with_checked_items(self):
        rf = RequestFactory()
        items = self.step_page.checklist_items.all()[:2]
        query = {'checklist': tuple(items.values_list('pk', flat=True))}
        request = rf.post('/', query)
        request.user = self.user
        request._dont_enforce_csrf_check = False
        form = forms.ChecklistForm(self.step_page, request.POST,
                                   project=self.project)
        self.assertTrue(form.is_valid())
        form.save()
        self.assertEqual(self.project.checklists.first().pk, self.step_page.pk)
        self.assertQuerysetEqual(
            self.project.checked_items.all(), items,
            ordered=False, transform=lambda x: x)


class UserFormTestCase(TestCase):

    def setUp(self):
        self.email = 'test@gmail.com'
        self.password = 'knew1for!'

    def test_create_user(self):
        """Checkbox items and form items should match"""

        initial_data = {'email': self.email,
                        'password1': self.password,
                        'password2': self.password}

        form = forms.CustomUserCreationForm(initial_data)
        self.assertTrue(form.is_valid())
        form.save()
        u = User.objects.get(email=self.email)
        self.assertEqual(u.username, self.email)


class BizLicenseFormTestCase(TestCase):

    def setUp(self):
        self.cu_id = 'CU-123-234'
        self.bad_cu_id = '123-234'

    def test_form_validates_cu(self):
        """Checkbox items and form items should match"""
        initial_data = {'cu_id': self.cu_id}
        form = forms.BizLicenseStatusForm(initial_data)
        self.assertTrue(form.is_valid())

    def test_form_raises_error_without_cu(self):
        initial_data = {'cu_id': self.bad_cu_id}
        form = forms.BizLicenseStatusForm(initial_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['cu_id'][0],
            "Your business license identifier must start with CU")
