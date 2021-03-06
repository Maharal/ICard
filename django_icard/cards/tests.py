from django.test import Client
from django.test import TestCase
from django.http import HttpRequest

from .views import favorite_card, home_page, login, signup

from django.contrib.auth.models import User

from .forms import CardForm, SignUpForm, EditUserForm

from .models import Card


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
        response = c.post('/cards/login/', {'username': 'jimhalpert', 'password': 'hEtz6Z78ZqM8dSRV'})
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

        form_data = {'name': 'Jim', 'description': 'World\'s second Best Boss', 'profile_image': 'link',
                     'contact_email': 'jimhalpert@dundermifflin.com', 'contact_phone': '31999999999',
                     'birthday': '1983-09-30'}
        form = CardForm(data=form_data)
        self.assertTrue(form.is_valid())
        form.save()

        cards = Card.objects.filter(contact_email='jimhalpert@dundermifflin.com')

        self.assertEqual(len(cards), 3)

        card_id = cards[2].id

        c = Client()
        response = c.post('/cards/edit_card/' + str(card_id) + '/',
                          {'name': 'Jim Dunder', 'description': 'World\'s second Best Boss',
                           'profile_image': 'link', 'contact_email': 'jimhalpert@dundermifflin.com',
                           'contact_phone': '31999999999', 'birthday': '1983-09-30'})
        self.assertEqual(response.status_code, 302)

        cards = Card.objects.filter(contact_email='jimhalpert@dundermifflin.com')
        card_name = cards[2].name
        self.assertEqual('Jim Dunder', card_name)

        self.assertEqual(len(cards), 3)

        # get card id
        cards = Card.objects.filter(contact_email='jimhalpert@dundermifflin.com')
        card_id = cards[0].id

        c = Client()
        response = c.post('/cards/card/' + str(card_id) + '/')
        self.assertEqual(response.status_code, 302)

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
        response = c.post('/cards/login/', {'username': 'jimhalpert', 'password': 'outrasenha'})
        self.assertNotEqual(response.status_code, 302)

        c = Client()
        response = c.post('/cards/login/', {'username': 'michael', 'password': 'hEtz6Z78ZqM8dSRV'})
        self.assertNotEqual(response.status_code, 302)

    def test_card_edit_name(self):
        form_data = {'name': 'Michael', 'description': 'World\'s Best Boss', 'profile_image': 'link',
                     'contact_email': 'michael@dundermifflin.com', 'contact_phone': '31999999999',
                     'birthday': '1983-09-30'}
        form = CardForm(data=form_data)
        self.assertTrue(form.is_valid())
        form.save()

        # get card id
        cards = Card.objects.filter(contact_email='michael@dundermifflin.com')
        card_id = cards[0].id

        c = Client()
        response = c.post('/cards/edit_card/' + str(card_id) + '/',
                          {'name': 'Michael Dunder', 'description': 'World\'s Best Boss', 'profile_image': 'link',
                           'contact_email': 'michael@dundermifflin.com', 'contact_phone': '31999999999',
                           'birthday': '1983-09-30'})
        self.assertEqual(response.status_code, 302)

        cards = Card.objects.filter(contact_email='michael@dundermifflin.com')
        card_name = cards[0].name
        self.assertEqual('Michael Dunder', card_name)

    def test_user_edit_name(self):
        form_data = {'username': 'jimhalpert', 'first_name': 'Jim', 'last_name': 'Halpert',
                     'email': 'jimhalpert@dundermifflin.com', 'password1': 'hEtz6Z78ZqM8dSRV',
                     'password2': 'hEtz6Z78ZqM8dSRV'}
        form = SignUpForm(data=form_data)
        self.assertTrue(form.is_valid())
        form.save()

        c = Client()
        response = c.post('/cards/login/', {'username': 'jimhalpert', 'password': 'hEtz6Z78ZqM8dSRV'})
        self.assertEqual(response.status_code, 302)

        users = User.objects.filter(username='jimhalpert')
        user_id = users[0].id

        form_data = {'username': 'jim_halpert', 'first_name': 'new jim', 'last_name': 'halpert',
                     'email': 'jimhalpert@dundermifflin.com'}
        form = EditUserForm(data=form_data, instance=users[0])
        self.assertTrue(form.is_valid(), True)

        response = c.post('/cards/profile/' + str(user_id) + '/', form_data)
        self.assertEqual(response.status_code, 200)

        users = User.objects.filter(username='jim_halpert')
        self.assertEqual(users[0].username, 'jim_halpert')
        self.assertEqual(users[0].first_name, 'new jim')
        self.assertEqual(users[0].last_name, 'halpert')
        self.assertEqual(users[0].email, 'jimhalpert@dundermifflin.com')

        users = User.objects.filter(username='jimhalpert')
        self.assertEqual(len(users), 0)

    def test_user_delete(self):
        form_data = {'username': 'jimhalpert', 'first_name': 'Jim', 'last_name': 'Halpert',
                     'email': 'jimhalpert@dundermifflin.com', 'password1': 'hEtz6Z78ZqM8dSRV',
                     'password2': 'hEtz6Z78ZqM8dSRV'}
        form = SignUpForm(data=form_data)
        self.assertTrue(form.is_valid())
        form.save()

        c = Client()
        response = c.post('/cards/login/', {'username': 'jimhalpert', 'password': 'hEtz6Z78ZqM8dSRV'})
        self.assertEqual(response.status_code, 302)

        users = User.objects.filter(username='jimhalpert')
        user_id = users[0].id

        response = c.post('/cards/delete_profile/' + str(user_id) + '/')
        self.assertEqual(response.status_code, 200)

        users = User.objects.filter(username='jimhalpert')
        self.assertEqual(len(users), 0)

    def test_card_edit_description(self):
        form_data = {'name': 'Michael', 'description': 'World\'s Best Boss', 'profile_image': 'link',
                     'contact_email': 'michael@dundermifflin.com', 'contact_phone': '31999999999',
                     'birthday': '1983-09-30'}
        form = CardForm(data=form_data)
        self.assertTrue(form.is_valid())
        form.save()

        # get card id
        cards = Card.objects.filter(contact_email='michael@dundermifflin.com')
        card_id = cards[0].id

        c = Client()
        response = c.post('/cards/edit_card/' + str(card_id) + '/',
                          {'name': 'Michael', 'description': 'World\'s Best Boss of 2020', 'profile_image': 'link',
                           'contact_email': 'michael@dundermifflin.com', 'contact_phone': '31999999999',
                           'birthday': '1983-09-30'})
        self.assertEqual(response.status_code, 302)

        cards = Card.objects.filter(contact_email='michael@dundermifflin.com')
        card_description = cards[0].description
        self.assertEqual('World\'s Best Boss of 2020', card_description)

    def test_card_edit_email(self):
        form_data = {'name': 'Michael', 'description': 'World\'s Best Boss', 'profile_image': 'link',
                     'contact_email': 'michael@dundermifflin.com', 'contact_phone': '31999999999',
                     'birthday': '1983-09-30'}
        form = CardForm(data=form_data)
        self.assertTrue(form.is_valid())
        form.save()

        # get card id
        cards = Card.objects.filter(contact_email='michael@dundermifflin.com')
        card_id = cards[0].id

        c = Client()
        response = c.post('/cards/edit_card/' + str(card_id) + '/',
                          {'name': 'Michael', 'description': 'World\'s Best Boss', 'profile_image': 'link',
                           'contact_email': 'michael@dunder.com', 'contact_phone': '31999999999',
                           'birthday': '1983-09-30'})
        self.assertEqual(response.status_code, 302)

        cards = Card.objects.filter(contact_email='michael@dundermifflin.com')
        self.assertEqual(len(cards), 0)

        cards = Card.objects.filter(contact_email='michael@dunder.com')
        self.assertEqual(len(cards), 1)

    def test_card_edit_birthday(self):
        form_data = {'name': 'Michael', 'description': 'World\'s Best Boss', 'profile_image': 'link',
                     'contact_email': 'michael@dundermifflin.com', 'contact_phone': '31999999999',
                     'birthday': '1983-09-30'}
        form = CardForm(data=form_data)
        self.assertTrue(form.is_valid())
        form.save()

        # get card id
        cards = Card.objects.filter(contact_email='michael@dundermifflin.com')
        card_id = cards[0].id

        c = Client()
        response = c.post('/cards/edit_card/' + str(card_id) + '/',
                          {'name': 'Michael', 'description': 'World\'s Best Boss', 'profile_image': 'link',
                           'contact_email': 'michael@dundermifflin.com', 'contact_phone': '31999999999',
                           'birthday': '1983-10-30'})
        self.assertEqual(response.status_code, 302)

        cards = Card.objects.filter(contact_email='michael@dundermifflin.com')
        card_birthday = cards[0].birthday
        self.assertEqual('1983-10-30', card_birthday.strftime('%Y-%m-%d'))

    def test_card_edit_birthday_fail_young(self):
        form_data = {'name': 'Michael', 'description': 'World\'s Best Boss', 'profile_image': 'link',
                     'contact_email': 'michael@dundermifflin.com', 'contact_phone': '31999999999',
                     'birthday': '1983-09-30'}
        form = CardForm(data=form_data)
        self.assertTrue(form.is_valid())
        form.save()

        # get card id
        cards = Card.objects.filter(contact_email='michael@dundermifflin.com')
        card_id = cards[0].id

        c = Client()
        response = c.post('/cards/edit_card/' + str(card_id) + '/',
                          {'name': 'Michael', 'description': 'World\'s Best Boss', 'profile_image': 'link',
                           'contact_email': 'michael@dundermifflin.com', 'contact_phone': '31999999999',
                           'birthday': '2018-10-30'})
        self.assertNotEqual(response.status_code, 302)

        cards = Card.objects.filter(contact_email='michael@dundermifflin.com')
        card_birthday = cards[0].birthday
        self.assertNotEqual('2018-10-30', card_birthday.strftime('%Y-%m-%d'))

    def test_card_edit_birthday_fail_old(self):
        form_data = {'name': 'Michael', 'description': 'World\'s Best Boss', 'profile_image': 'link',
                     'contact_email': 'michael@dundermifflin.com', 'contact_phone': '31999999999',
                     'birthday': '1983-09-30'}
        form = CardForm(data=form_data)
        self.assertTrue(form.is_valid())
        form.save()

        # get card id
        cards = Card.objects.filter(contact_email='michael@dundermifflin.com')
        card_id = cards[0].id

        c = Client()
        response = c.post('/cards/edit_card/' + str(card_id) + '/',
                          {'name': 'Michael', 'description': 'World\'s Best Boss', 'profile_image': 'link',
                           'contact_email': 'michael@dundermifflin.com', 'contact_phone': '31999999999',
                           'birthday': '1800-10-30'})
        self.assertNotEqual(response.status_code, 302)

        cards = Card.objects.filter(contact_email='michael@dundermifflin.com')
        card_birthday = cards[0].birthday
        self.assertNotEqual('1800-10-30', card_birthday.strftime('%Y-%m-%d'))

    def test_card_edit_birthday_fail_short_phone(self):
        form_data = {'name': 'Michael', 'description': 'World\'s Best Boss', 'profile_image': 'link',
                     'contact_email': 'michael@dundermifflin.com', 'contact_phone': '31999999999',
                     'birthday': '1983-09-30'}
        form = CardForm(data=form_data)
        self.assertTrue(form.is_valid())
        form.save()

        # get card id
        cards = Card.objects.filter(contact_email='michael@dundermifflin.com')
        card_id = cards[0].id

        c = Client()
        response = c.post('/cards/edit_card/' + str(card_id) + '/',
                          {'name': 'Michael', 'description': 'World\'s Best Boss', 'profile_image': 'link',
                           'contact_email': 'michael@dundermifflin.com', 'contact_phone': '991',
                           'birthday': '1983-09-30'})
        self.assertNotEqual(response.status_code, 302)

        cards = Card.objects.filter(contact_email='michael@dundermifflin.com')
        card_phone = cards[0].contact_phone
        self.assertNotEqual('991', card_phone)

    def test_card_edit_birthday_fail_long_phone(self):
        form_data = {'name': 'Michael', 'description': 'World\'s Best Boss', 'profile_image': 'link',
                     'contact_email': 'michael@dundermifflin.com', 'contact_phone': '31999999999',
                     'birthday': '1983-09-30'}
        form = CardForm(data=form_data)
        self.assertTrue(form.is_valid())
        form.save()

        # get card id
        cards = Card.objects.filter(contact_email='michael@dundermifflin.com')
        card_id = cards[0].id

        c = Client()
        response = c.post('/cards/edit_card/' + str(card_id) + '/',
                          {'name': 'Michael', 'description': 'World\'s Best Boss', 'profile_image': 'link',
                           'contact_email': 'michael@dundermifflin.com', 'contact_phone': '123431999999999',
                           'birthday': '1983-09-30'})
        self.assertNotEqual(response.status_code, 302)

        cards = Card.objects.filter(contact_email='michael@dundermifflin.com')
        card_phone = cards[0].contact_phone
        self.assertNotEqual('123431999999999', card_phone)

    def test_card_delete_card(self):
        form_data = {'name': 'Michael', 'description': 'World\'s Best Boss', 'profile_image': 'link',
                     'contact_email': 'michael@dundermifflin.com', 'contact_phone': '31999999999',
                     'birthday': '1983-09-30'}
        form = CardForm(data=form_data)
        self.assertTrue(form.is_valid())
        form.save()

        # get card id
        cards = Card.objects.filter(contact_email='michael@dundermifflin.com')
        card_id = cards[0].id

        c = Client()
        response = c.post('/cards/card/' + str(card_id) + '/')
        self.assertEqual(response.status_code, 302)

        cards = Card.objects.filter(contact_email='michael@dundermifflin.com')
        self.assertEqual(len(cards), 0)

    def test_favorite_cards(self):
        form_data = {'username': 'jimhalpert', 'first_name': 'Jim', 'last_name': 'Halpert',
                     'email': 'jimhalpert@dundermifflin.com', 'password1': 'hEtz6Z78ZqM8dSRV',
                     'password2': 'hEtz6Z78ZqM8dSRV'}
        form = SignUpForm(data=form_data)
        self.assertTrue(form.is_valid())
        form.save()

        c = Client()
        response = c.post('/cards/login/', {'username': 'jimhalpert', 'password': 'hEtz6Z78ZqM8dSRV'})
        self.assertEqual(response.status_code, 302)

        users = User.objects.filter(username='jimhalpert')

        form_data = {'name': 'Michael', 'description': 'World\'s Best Boss', 'profile_image': 'link',
                     'contact_email': 'michael@dundermifflin.com', 'contact_phone': '31999999999',
                     'birthday': '1983-09-30'}
        form = CardForm(data=form_data)
        self.assertTrue(form.is_valid())
        form.save()

        # get card id
        cards = Card.objects.filter(contact_email='michael@dundermifflin.com')
        card_id = cards[0].id

        cards = Card.objects.filter(favorited_users=users[0])
        self.assertEqual(len(cards), 0)

        response = c.post('/cards/favorite_card/' + str(card_id) + '/')
        self.assertEqual(response.status_code, 302)

        cards = Card.objects.filter(favorited_users=users[0])
        self.assertNotEqual(len(cards), 0)


    def test_card_search(self):
        form_data = {'name': 'Michael', 'description': 'World\'s Best Boss', 'profile_image': 'link',
                     'contact_email': 'michael@dundermifflin.com', 'contact_phone': '31999999999',
                     'birthday': '1983-09-30'}
        form = CardForm(data=form_data)
        self.assertTrue(form.is_valid())
        form.save()
        c = Client()
        response = c.post('/cards/search/', {'search': 'Mich'})
        self.assertNotIn("Nenhum card encontrado!", response.content.decode('utf-8'))

        response = c.post('/cards/search/', {'search': 'Pam'})
        self.assertIn("Nenhum card encontrado!", response.content.decode('utf-8'))
