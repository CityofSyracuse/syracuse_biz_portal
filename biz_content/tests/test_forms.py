from . import factories
from biz_content import models, forms
from django.test import TransactionTestCase, TestCase
from django.core.urlresolvers import reverse
import pdb


class CheckListFormTestCase(TransactionTestCase):

    def setUp(self):
        self.project = factories.ProjectFactory()
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


class UserFormTestCase(TransactionTestCase):

    def setUp(self):
        self.email = 'test@gmail.com'
        self.password1 = 'knew1for!'
        self.password2 = 'knew1for!'

    # def test_init(self):
    #     forms.CustomUserCreationForm(entry=self.entry)

    def test_create_user(self):
        """Checkbox items and form items should match"""

        initial_data = {'email': self.email,
                    'password1': self.password1,
                    'password2': self.password2}

        form = forms.CustomUserCreationForm(initial_data)

        self.assertTrue(form.is_valid())

