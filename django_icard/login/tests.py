from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from login.views import home_page, login, signup

class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertTrue(html.endswith('</html>'))

class LoginTest(TestCase):

    def test_login_page_has_email_fild(self):
        request = HttpRequest()
        response = login(request)
        html = response.content.decode('utf8')
        self.assertIn('<input type="email" class="form-control " id="email" name="email" placeholder=" ">', html)

    def test_login_page_has_password_fild(self):
        request = HttpRequest()
        response = login(request)
        html = response.content.decode('utf8')
        self.assertIn('<input type="password" class="form-control" id="password" name="password" minlength="8" placeholder=" ">', html)

class SignupTest(TestCase):

    def test_signup_page_has_email_fild(self):
        request = HttpRequest()
        response = signup(request)
        html = response.content.decode('utf8')
        self.assertIn('<input type="email" class="form-control" id="email" name="email" placeholder=" ">', html)

    def test_signup_page_has_password_fild(self):
        request = HttpRequest()
        response = signup(request)
        html = response.content.decode('utf8')
        self.assertIn('<input type="password" class="form-control" id="password" name="password" minlength="8" placeholder=" ">', html)
