import datetime
import re

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from json import dumps

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import SignUpForm, CardForm
from .models import Card


# Create your views here.
def home_page(request):
    cards = Card.objects.filter(user=request.user.id)
    print(cards)
    return render(request, 'home.html', {'cards': cards})


def login(request):
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/cards/login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def profile(request):
    return render(request, 'profile.html')


def get_card(request):
    if request.method == 'POST':
        form = CardForm(request.POST, request.FILES)
        if form.is_valid() and request.user.is_authenticated:

            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('/cards')

    else:
        form = CardForm()

    return render(request, 'new_card.html', {'form': form})

def card(request, card_id):
    cards = Card.objects.filter(id=card_id)
    print(cards[0])
    return render(request, 'single_card.html', {'card': cards[0]})


def get_all_cards(request):
    cards = Card.objects.all()
    print("Testando")
    return render(request, 'home.html', {'cards': cards})


def get_user_cards(request):
    cards = Card(user=request.user)
    return render(request, 'home.html', {'cards': dumps(cards)})

def edit_card(request, card_id):
    cards = Card.objects.filter(id=card_id)
    print(cards[0])
    return render(request, 'edit_card.html', {'card': cards[0]})

def update_card(request, id):
    card = Card(id=id)
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            card.name = form.name
            card.description = form.description
            card.profile_image = form.profile_image
            card.save()
            return render(request, 'home.html')
    else:
        form = CardForm()
        form.name = card.name
        form.description = card.description
        form.profile_image = card.profile_image
        return render(request, 'new_card.html', {'form': form})


def remove_card(request, id):
    card = Card(id=id)
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            card.name = form.name
            card.description = form.description
            card.profile_image = form.profile_image
            card.save()
            return render(request, 'home.html')
    else:
        form = CardForm()
        form.name = card.name
        form.description = card.description
        form.profile_image = card.profile_image
        return render(request, 'new_card.html', {'form': form})
