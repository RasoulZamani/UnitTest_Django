from django.test import TestCase
from accounts.forms import UserRegisterForm
from django.contrib.auth.models import User
from model_bakery import baker


class TestRegisterForm(TestCase):
    """ tsting methods in registration form"""
    def test_valid_data(self):
        """form ahould be valid"""
        form = UserRegisterForm(data={'username':'ali',
            'email':'ali@email.com', 'password':'ali'})
        self.assertTrue(form.is_valid())
        
    def test_empty_data(self):
        """empty data should raise error"""
        form = UserRegisterForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)
        
    def test_email_already_exists(self):
        """email should be unique"""
        user = baker.make(User, username='ali2', email='ali2@email.com')
        #user = User.objects.create_user(username='ali2', email='ali2@email.com',password='ali2')
        form = UserRegisterForm(data={'username': 'not_ali2', 'email':'ali2@email.com','password':'ali3'})
        self.assertEqual(len(form.errors), 1)
        self.assertTrue(form.has_error('email'))        
        
        
    