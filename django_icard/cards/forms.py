import datetime
import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import Card


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class EditUserForm(UserChangeForm):

    def __init__(self, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)
        del self.fields['password']

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class CardForm(forms.ModelForm):
    name = forms.CharField(label='name', max_length=100)
    description = forms.CharField(label='description', max_length=280)
    profile_image = forms.FileField(label='profile_image', required=False)
    contact_email = forms.CharField(label='contact_email', max_length=280)
    contact_phone = forms.CharField(label='contact_phone', max_length=280)
    birthday = forms.CharField(label='birthday', max_length=280)

    def clean_contact_phone(self):
        data = self.cleaned_data['contact_phone']
        phone = re.sub("[^0-9]", "", data)  # only numbers

        if len(phone) < 8 or len(phone) > 13:
            raise ValidationError(_('Invalid phone'))

        return phone

    def clean_birthday(self):
        data = self.cleaned_data['birthday']
        year = int(data[0:4])
        month = int(data[5:7])
        day = int(data[8:])
        birth = datetime.datetime(year, month, day)
        age = datetime.datetime.now() - birth

        if age.days > 365 * 100 or age.days < 365 * 16:
            raise ValidationError(_('Invalid date - age must be between 16 and 100 years'))

        return data

    class Meta:
        model = Card
        exclude = ['user', ]
        fields = ('name', 'description', 'profile_image', 'contact_email', 'contact_phone', 'birthday')
