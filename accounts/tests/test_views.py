from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.shortcuts import reverse
from accounts.forms import UserRegisterForm


class TestUserRegView(TestCase):
    def setUp(self):
        self.client = Client()
        
    def test_user_reg_GET(self):
        """ get method in view"""
        response = self.client.get(reverse('accounts:user_register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/home.html')
        self.failUnless(response.context['register_form'], UserRegisterForm)
        
    def test_user_reg_POST_valid(self):
        """ test valid post method in view"""
        response = self.client.post(reverse('accounts:user_register'), data={'username':'ali',
                'email':'ali@email.com','password':'alipass'})
        self.assertEqual(response.status_code, 302) 
        self.assertRedirects(response, reverse('home:home'))
        self.assertEqual(User.objects.count(), 1)
        
    def test_user_reg_POST_invalid(self):
        """ test invalid post method in view"""
        response = self.client.post(reverse('accounts:user_register'), data={'username':'ali2',
                'email':'invalid', 'password':'ali2pass'})
        self.assertEqual(response.status_code, 200) 
        self.failIf(response.context['register_form'].is_valid())
        self.assertFormError(form=response.context['register_form'],
                             field='email', errors=['Enter a valid email address.'])
        