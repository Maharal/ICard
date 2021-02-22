from django.conf.urls import url
from .views import home_page, signup, profile, get_card, get_all_cards


urlpatterns = [
    url(r'^$', home_page, name='home'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^get_card/$', get_card, name='get_card'),
    url(r'^get_all_cards/$', get_all_cards, name='get_all_cards'),
]