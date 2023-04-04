from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import HomeView

class TestUrl(SimpleTestCase):
    """is url conndcted to correct view?"""
    def test_homeview(self):
        url = reverse('home:home')
        self.assertEqual(resolve(url).func.view_class, HomeView)
        