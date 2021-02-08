from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from .views import home_page, login, signup

from .forms import CardForm, SignUpForm

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

    def test_signup_page_has_first_name_fild(self):
        request = HttpRequest()
        response = signup(request)
        html = response.content.decode('utf8')
        self.assertIn('<input type="text" class="form-control" id="id_first_name" name="first_name" placeholder=" ">', html)

    def test_signup_page_has_last_name_fild(self):
        request = HttpRequest()
        response = signup(request)
        html = response.content.decode('utf8')
        self.assertIn('<input type="text" class="form-control" id="id_last_name" name="last_name" placeholder=" ">', html)

    def test_signup_page_has_username_fild(self):
        request = HttpRequest()
        response = signup(request)
        html = response.content.decode('utf8')
        self.assertIn('<input type="text" class="form-control" id="id_last_name" name="last_name" placeholder=" ">', html)

    def test_signup_page_has_email_fild(self):
        request = HttpRequest()
        response = signup(request)
        html = response.content.decode('utf8')
        self.assertIn('<input type="email" class="form-control" id="id_email" name="email" placeholder=" ">', html)

    def test_signup_page_has_password_fild(self):
        request = HttpRequest()
        response = signup(request)
        html = response.content.decode('utf8')
        self.assertIn('<input type="password" class="form-control" id="id_password1" name="password1" minlength="8" placeholder=" ">', html)

    def test_signup_page_has_password_confirmation_fild(self):
        request = HttpRequest()
        response = signup(request)
        html = response.content.decode('utf8')
        self.assertIn('<input type="password" class="form-control" id="id_password2" name="password2" minlength="8" placeholder=" ">', html)

class SignUpFormTest(TestCase):
    def test_form_success(self):
        form_data = {'username': 'Joseph123', 'first_name': 'Joseph', 'last_name': 'Klimber', 'email': 'joseph@klimber.com', 'password1': 'senha123456', 'password2': 'senha123456'}
        form = SignUpForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_incomplete_form(self):
        form_data = {'username': 'Joseph123', 'first_name': 'Joseph', 'last_name': 'Klimber', 'email': 'joseph@klimber.com', 'password1': 'senha123456'} # missing password2
        form = SignUpForm(data=form_data)
        self.assertFalse(form.is_valid())

class CardTests(TestCase):
    def test_form_success(self):
        form_data = {'name': 'Michael', 'description': 'World\'s Best Boss', 'profile_image': 'link'}
        form = CardForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_fail(self):
        form_data = {'name': 'Toby', 'profile_image': 'link'}  # missing description
        form = CardForm(data=form_data)
        self.assertFalse(form.is_valid())
