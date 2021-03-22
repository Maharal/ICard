from json import dumps

from django.shortcuts import render, redirect

from .forms import SignUpForm, CardForm
from .models import Card
from django.contrib.auth.models import User


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


def profile(request, user_id):
    user = User.objects.filter(id=user_id)
    if request.method == 'POST':
        return render(request, 'profile.html', {'user': user[0]})
    else:
        return render(request, 'profile.html', {'user': user[0]})


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
    if request.method == 'POST':  # Delete card
        card = cards[0]
        card.delete()
        return redirect('/cards')
    return render(request, 'single_card.html', {'card': cards[0]})


def get_all_cards(request):
    cards = Card.objects.all()
    return render(request, 'home.html', {'cards': cards})


def get_user_cards(request):
    cards = Card(user=request.user)
    return render(request, 'home.html', {'cards': dumps(cards)})


def edit_card(request, card_id):
    cards = Card.objects.filter(id=card_id)
    if request.method == 'POST':
        card = cards[0]
        form = CardForm(request.POST, request.FILES)
        if form.is_valid():
            card.name = form.cleaned_data['name']
            card.description = form.cleaned_data['description']
            card.birthday = form.cleaned_data['birthday']
            card.contact_email = form.cleaned_data['contact_email']
            card.contact_phone = form.cleaned_data['contact_phone']

            if form.cleaned_data['profile_image'] is not None:
                card.profile_image = form.cleaned_data['profile_image']

            card.save()
            return redirect('/cards')
        return render(request, 'edit_card.html', {'card': cards[0]})
    else:
        return render(request, 'edit_card.html', {'card': cards[0]})
