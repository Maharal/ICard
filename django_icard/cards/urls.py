from django.conf.urls import url
from .views import edit_card, home_page, signup, profile, delete_profile, get_card, get_all_cards, card, \
    all_favorite_cards, favorite_card, remove_favorite_card, search


urlpatterns = [
    url(r'^$', home_page, name='home'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^profile/(?P<user_id>\d+)/$', profile, name='profile'),
    url(r'^search/$', search, name='search'),
    url(r'^delete_profile/(?P<user_id>\d+)/$', delete_profile, name='delete_profile'),
    url(r'^get_card/$', get_card, name='get_card'),
    url(r'^get_all_cards/$', get_all_cards, name='get_all_cards'),
    url(r'^card/(?P<card_id>\d+)/$', card, name='card'),
    url(r'^edit_card/(?P<card_id>\d+)/$', edit_card, name='edit_card'),
    url(r'^all_favorite_cards/$', all_favorite_cards, name='all_favorite_cards'),
    url(r'^favorite_card/(?P<card_id>\d+)/$', favorite_card, name='favorite_card'),
    url(r'^remove_favorite_card/(?P<card_id>\d+)/$', remove_favorite_card, name='remove_favorite_card'),
]