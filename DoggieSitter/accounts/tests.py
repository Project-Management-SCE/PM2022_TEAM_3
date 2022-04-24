from django.test import TestCase
from django.urls import reverse
from . import models
import re


class BasicTests(TestCase):
    def test_hello(self):
        print('hello world')
    def test_firstname(self):
        print('test1')
        acc = models.Accounts()
        acc.first_name = 'Moran'
        self.assertTrue(len(acc.id) <= 9, 'Check name is less than 50 digits long')
        self.assertFalse(len(acc.id) > 50, 'Check name is less than 50 digits long')

    def test_lastname(self):
        print('test2')
        acc = models.Accounts()
        acc.last_name = 'Shalvi'
        self.assertFalse(len(acc.id) > 50, 'Check name is less than 50 digits long')

    def test_id(self):
        print('test3')
        acc = models.Accounts()
        acc.id = '123456789'
        self.assertTrue(len(acc.id) == 9, 'Check ID is 9 digits long')

    def test_email(self):
        print('test4')
        acc = models.Accounts()
        acc.email = 'Nadavg@mail.com'
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        self.assertTrue(re.fullmatch(regex, acc.email), 'check email format is valid')
        acc.email = 'Nadavgmail.com'
        self.assertFalse(re.fullmatch(regex, acc.email), 'check email format is valid')

    def test_gender(self):
        print('test5')
        genders = ['male', 'female']
        acc = models.Accounts()
        acc.gender = 'female'
        self.assertTrue(acc.gender in genders, ' gender test ')
        acc.gender = 'unknown'
        self.assertFalse(acc.gender in genders, 'gender test2')

    def test_Date(self):
        print('test6')
        acc = models.Accounts()
        acc.phone_number = '0526203790'
        self.assertEqual(acc.phone_number[0], '0', 'First digit is 0')
        self.assertEqual(acc.phone_number[1], '5', 'Second digit is 5')
        self.assertTrue(len(acc.phone_number) == 10, 'Check ID is 10 digits long1')
        acc.phone_number = '052620370'
        self.assertFalse(len(acc.phone_number) == 10, 'Check ID is 10 digits long2')

    def test_address(self):
        print('test7')
        acc = models.Accounts()
        acc.address = 'One Apple Park Way, Cupertino, CA 95014, United States'
        self.assertFalse(len(acc.address) <= 50, 'Check name is less than 50 digits long1')
        acc.address = 'One Apple Park Way, Cupertino, CA 95014, United States'
        self.assertTrue(len(acc.address) > 50, 'Check name is less than 50 digits long2')


class BaseTest(TestCase):
    def setUp(self):
        self.signup_url = reverse('signup')
        return super().setUp()


class signUpTest(BaseTest):
    def can_view(self):
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')
