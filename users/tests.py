from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import CustomUser
from django.urls import reverse, reverse_lazy
# Create your tests here.
class TestLoginView(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='ali',
            email='ali@gmail.com',
            password='password'
        )

        self.user2 = get_user_model().objects.create_user(
            username='alawi',
            email='ali@gmail.com',
            password='password'
        )

    def test_the_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)

    # def test_the_view(self):
    #     response = self.client.post(reverse_lazy('login'))
    #     self.assertEqual(response.status_code,200)
    