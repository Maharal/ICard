from django.conf.urls import url
from .views import signup, profile, get_card


urlpatterns = [
    url(r'^signup/$', signup, name='signup'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^get_card/$', get_card, name='get_card'),
]