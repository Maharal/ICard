from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import SignUpForm, CardForm

# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def profile(request):
    return render(request, 'profile.html')

def get_card(request):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            print("Válido!")
            return render(request, 'home.html')

    else:
        form = CardForm()

    return render(request, 'new_card.html', {'form': form})
