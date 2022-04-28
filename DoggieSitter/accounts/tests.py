from Tools.scripts import generate_token
from django.test import TestCase
from django.urls import reverse, path, include
from django.contrib.auth.models import User
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from . import models, views
import re
from django.urls import reverse

from django.contrib import auth
from django.http import HttpRequest
from django.shortcuts import render
from django.template.loader import render_to_string
from django.contrib.auth import SESSION_KEY



class BasicTests(TestCase):
    def test_firstname(self):
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
        acc = models.Accounts()
        acc.id = '123456789'
        self.assertTrue(len(acc.id) == 9, 'Check ID is 9 digits long')

    def test_email(self):
        acc = models.Accounts()
        acc.email = 'Nadavg@mail.com'
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        self.assertTrue(re.fullmatch(regex, acc.email), 'check email format is valid')
        acc.email = 'Nadavgmail.com'
        self.assertFalse(re.fullmatch(regex, acc.email), 'check email format is valid')

    def test_gender(self):
        genders = ['male', 'female']
        acc = models.Accounts()
        acc.gender = 'female'
        self.assertTrue(acc.gender in genders, ' gender test ')
        acc.gender = 'unknown'
        self.assertFalse(acc.gender in genders, 'gender test2')

    def test_Date(self):
        acc = models.Accounts()
        acc.phone_number = '0526203790'
        self.assertEqual(acc.phone_number[0], '0', 'First digit is 0')
        self.assertEqual(acc.phone_number[1], '5', 'Second digit is 5')
        self.assertTrue(len(acc.phone_number) == 10, 'Check ID is 10 digits long1')
        acc.phone_number = '052620370'
        self.assertFalse(len(acc.phone_number) == 10, 'Check ID is 10 digits long2')

    def test_address(self):
        acc = models.Accounts()
        acc.address = 'One Apple Park Way, Cupertino, CA 95014, United States'
        self.assertFalse(len(acc.address) <= 50, 'Check name is less than 50 digits long1')
        acc.address = 'One Apple Park Way, Cupertino, CA 95014, United States'
        self.assertTrue(len(acc.address) > 50, 'Check name is less than 50 digits long2')


class BaseTest(TestCase):
    def setUp(self):
        self.login_url = reverse('login')
        self.home = reverse('home')
        self.user = {
            'username': 'bobo',
            'password': '123456bo',
        }
        self.test = {
            'username': 'bobo',
            'password': '123456bo',
        }
        self.unmatching_user = {
            'username': 'username',
            'password': 'password',
        }
        self.user_unmatching_password = {
            'username': 'username',
            'password': 'teslatt',
        }
        return super().setUp()

    def test_Logged(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'userpass'
        }
        user = User.objects.create_user(**self.credentials)
        login = self.client.login(username='testuser', password='userpass')
        self.assertTrue(login)


class InsertInfoTest(BaseTest):
    def test_can_view_page_correctly(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_password_incorrect(self):
        response = self.client.post(self.login_url, self.user_unmatching_password, format='text/html')
        self.assertTemplateUsed(response, 'registration/login.html')
        self.assertEqual(response.status_code, 200)

    def test_user_incorrect(self):
        response = self.client.post(self.login_url, self.unmatching_user, format='text/html')
        self.assertTemplateUsed(response, 'registration/login.html')
        self.assertEqual(response.status_code, 200)


class LogInTest(TestCase):

    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': '5t4r3e2w1q',
        }
        user = User.objects.create_user(**self.credentials)
        user.is_active = True

    def test_login(self):
        response = self.client.post('/accounts/login/', **self.credentials, follow=True)
        status = response.context['user'].is_active
        self.assertFalse(status)

    def test_logout(self):
        response = self.client.post('/accounts/login/', **self.credentials, follow=True)
        self.assertFalse(response.context['user'].is_active)



class DeleteUser(TestCase):
    def test_delete(self):
        self.credentials = {
            'username': 'testuser',
            'email': 'user@gmail.com',
            'password': 'userpassdskfldskf'
        }
        user = User.objects.create_user(**self.credentials)
        us = User.objects.get(username=user)
        us.delete()
        self.assertFalse(User.objects.filter(username=us).exists())


class CreateTypeUser(TestCase):
    def test_create_Doggie_approved(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'userpassdskfldskf',
            'first_name': 'test',
            'last_name': 'unit',
        }
        user = User.objects.create_user(**self.credentials)
        acc = models.Accounts(user)
        acc.is_doggiesitter= True
        acc.approved = True
        isDoggie = acc.is_doggiesitter
        isApproved= acc.approved
        self.assertTrue(isDoggie)
        self.assertFalse(not isApproved)

    def test_create_Doggie_not_approved(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'userpassdskfldskf',
            'first_name': 'test',
            'last_name': 'unit',
        }
        user = User.objects.create_user(**self.credentials)
        acc = models.Accounts(user)
        acc.is_doggiesitter= True
        acc.approved = False
        isDoggie = acc.is_doggiesitter
        isApproved= acc.approved
        self.assertTrue(isDoggie)
        self.assertFalse(isApproved)

    def test_create_Owner(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'userpassdskfldskf',
            'first_name': 'test',
            'last_name': 'unit',
        }
        user = User.objects.create_user(**self.credentials)
        acc = models.Accounts(user)
        acc.is_doggiesitter= False
        isDoggie = acc.is_doggiesitter
        self.assertFalse(isDoggie)



class EditUser(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'userpassdskfldskf',
            'first_name': 'test',
            'last_name': 'unit',
        }

    def test_Changeinfo_Username(self):
        user = User.objects.create_user(**self.credentials)
        us = User.objects.filter(pk=user.id).first()
        us.username = 'newname'
        self.assertNotEqual(us.username,'testuser')


    def test_Changeinfo_password(self):
        user = User.objects.create_user(**self.credentials)
        us = User.objects.filter(pk=user.id).first()
        us.set_password('pass')
        self.assertNotEqual(us.password, 'testuser')

    def test_Changeinfo_First_Name(self):
        user = User.objects.create_user(**self.credentials)
        us = User.objects.filter(pk=user.id).first()
        us.first_name = 'newname'
        self.assertNotEqual(us.username, 'test')

    def test_Changeinfo_Last_Name(self):
        user = User.objects.create_user(**self.credentials)
        us = User.objects.filter(pk=user.id).first()
        us.last_name = 'newname'
        self.assertNotEqual(us.username, 'unit')









