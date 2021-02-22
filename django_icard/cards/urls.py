from django.conf.urls import url
from .views import edit_card, home_page, signup, profile, get_card, get_all_cards, card


urlpatterns = [
    url(r'^$', home_page, name='home'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^get_card/$', get_card, name='get_card'),
    url(r'^get_all_cards/$', get_all_cards, name='get_all_cards'),
    url(r'^card/(?P<card_id>\d+)/$', card, name='card'),
    url(r'^edit_card/(?P<card_id>\d+)/$', edit_card, name='edit_card'),
]