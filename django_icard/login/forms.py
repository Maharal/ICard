from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Card


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class CardForm(forms.ModelForm):
    name = forms.CharField(label='name', max_length=100)
    description = forms.CharField(label='description', max_length=280)
    profile_image = forms.CharField(label='profile_image', max_length=280)
    contact_email = forms.CharField(label='contact_email', max_length=280)
    contact_phone = forms.CharField(label='contact_phone', max_length=280)
    birthday = forms.CharField(label='birthday', max_length=280)

    class Meta:
        model = Card
        exclude = ['user', ]
        fields = ('name', 'description', 'profile_image', 'contact_email', 'contact_phone', 'birthday')
