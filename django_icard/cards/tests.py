from django.test import Client
from django.test import TestCase
from django.http import HttpRequest

from .views import home_page, login, signup

from .forms import CardForm, SignUpForm

from .models import Card


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
        self.assertIn(
            '<input type="password" class="form-control" id="password" name="password" minlength="8" placeholder=" ">',
            html)


class SignupTest(TestCase):

    def test_signup_page_has_first_name_fild(self):
        request = HttpRequest()
        response = signup(request)
        html = response.content.decode('utf8')
        self.assertIn('<input type="text" class="form-control" id="id_first_name" name="first_name" placeholder=" ">',
                      html)

    def test_signup_page_has_last_name_fild(self):
        request = HttpRequest()
        response = signup(request)
        html = response.content.decode('utf8')
        self.assertIn('<input type="text" class="form-control" id="id_last_name" name="last_name" placeholder=" ">',
                      html)

    def test_signup_page_has_username_fild(self):
        request = HttpRequest()
        response = signup(request)
        html = response.content.decode('utf8')
        self.assertIn('<input type="text" class="form-control" id="id_last_name" name="last_name" placeholder=" ">',
                      html)

    def test_signup_page_has_email_fild(self):
        request = HttpRequest()
        response = signup(request)
        html = response.content.decode('utf8')
        self.assertIn('<input type="email" class="form-control" id="id_email" name="email" placeholder=" ">', html)

    def test_signup_page_has_password_fild(self):
        request = HttpRequest()
        response = signup(request)
        html = response.content.decode('utf8')
        self.assertIn(
            '<input type="password" class="form-control" id="id_password1" name="password1" minlength="8" placeholder=" ">',
            html)

    def test_signup_page_has_password_confirmation_fild(self):
        request = HttpRequest()
        response = signup(request)
        html = response.content.decode('utf8')
        self.assertIn(
            '<input type="password" class="form-control" id="id_password2" name="password2" minlength="8" placeholder=" ">',
            html)


class SignUpFormTest(TestCase):
    def test_form_success(self):
        form_data = {'username': 'Joseph123', 'first_name': 'Joseph', 'last_name': 'Klimber',
                     'email': 'joseph@klimber.com', 'password1': 'senha123456', 'password2': 'senha123456'}
        form = SignUpForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_incomplete_form(self):
        form_data = {'username': 'Joseph123', 'first_name': 'Joseph', 'last_name': 'Klimber',
                     'email': 'joseph@klimber.com', 'password1': 'senha123456'}  # missing password2
        form = SignUpForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_short_password(self):
        form_data = {'username': 'Joseph123', 'first_name': 'Joseph', 'last_name': 'Klimber',
                     'email': 'joseph@klimber.com', 'password1': 'senha123',
                     'password2': 'senha123'}  # password min length = 8
        form = SignUpForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_unmatching_passwords(self):
        form_data = {'username': 'Joseph123', 'first_name': 'Joseph', 'last_name': 'Klimber',
                     'email': 'joseph@klimber.com', 'password1': 'senha123', 'password2': 'senha456'}
        form = SignUpForm(data=form_data)
        self.assertFalse(form.is_valid())


class CardTests(TestCase):
    def test_form_success(self):
        form_data = {'name': 'Michael', 'description': 'World\'s Best Boss', 'profile_image': 'link',
                     'contact_email': 'michael@dundermifflin.com', 'contact_phone': '31999999999',
                     'birthday': '1983-09-30'}
        form = CardForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_fail_phone(self):
        form_data = {'name': 'Michael', 'description': 'World\'s Best Boss', 'profile_image': 'link',
                     'contact_email': 'michael@dundermifflin.com', 'contact_phone': '931', 'birthday': '1983-09-30'}
        form = CardForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_fail_birthday(self):
        form_data = {'name': 'Michael', 'description': 'World\'s Best Boss', 'profile_image': 'link',
                     'contact_email': 'michael@dundermifflin.com', 'contact_phone': '31999999999',
                     'birthday': '2010-09-30'}
        form = CardForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_fail_both_phone_birthday(self):
        form_data = {'name': 'Michael', 'description': 'World\'s Best Boss', 'profile_image': 'link',
                     'contact_email': 'michael@dundermifflin.com', 'contact_phone': '931', 'birthday': '2010-09-30'}
        form = CardForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_fail(self):
        form_data = {'name': 'Toby', 'profile_image': 'link'}  # missing fields
        form = CardForm(data=form_data)
        self.assertFalse(form.is_valid())


class IntegrationTests(TestCase):
    def test_signup_login_and_card_creation_success(self):
        form_data = {'username': 'jimhalpert', 'first_name': 'Jim', 'last_name': 'Halpert',
                     'email': 'jimhalpert@dundermifflin.com', 'password1': 'hEtz6Z78ZqM8dSRV',
                     'password2': 'hEtz6Z78ZqM8dSRV'}
        form = SignUpForm(data=form_data)
        self.assertTrue(form.is_valid())
        form.save()

        c = Client()
        response = c.post('/login/login/', {'username': 'jimhalpert', 'password': 'hEtz6Z78ZqM8dSRV'})
        self.assertEqual(response.status_code, 302)

        form_data = {'name': 'Jim', 'description': 'The best paper salesman', 'profile_image': 'image/185388.png',
                     'contact_email': 'jimhalpert@dundermifflin.com', 'contact_phone': '31999999999',
                     'birthday': '1983-09-30'}
        form = CardForm(data=form_data)
        self.assertTrue(form.is_valid())
        form.save()

        form_data = {'name': 'Jim Halpert', 'description': 'The best paper salesman in PA',
                     'profile_image': 'image/185388.png', 'contact_email': 'jimhalpert@dundermifflin.com',
                     'contact_phone': '31999999999', 'birthday': '1983-09-30'}
        form = CardForm(data=form_data)
        self.assertTrue(form.is_valid())
        form.save()

        cards = Card.objects.filter(contact_email='jimhalpert@dundermifflin.com')
        self.assertEqual(len(cards), 2)

    def test_signup_and_login_fail(self):
        form_data = {'username': 'jimhalpert', 'first_name': 'Jim', 'last_name': 'Halpert',
                     'email': 'jimhalpert@dundermifflin.com', 'password1': 'hEtz6Z78ZqM8dSRV',
                     'password2': 'hEtz6Z78ZqM8dSRV'}
        form = SignUpForm(data=form_data)
        self.assertTrue(form.is_valid())
        form.save()

        c = Client()
        response = c.post('/login/login/', {'username': 'jimhalpert', 'password': 'outrasenha'})
        self.assertNotEqual(response.status_code, 302)

        c = Client()
        response = c.post('/login/login/', {'username': 'michael', 'password': 'hEtz6Z78ZqM8dSRV'})
        self.assertNotEqual(response.status_code, 302)