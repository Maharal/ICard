from django.conf.urls import url
from .views import signup, profile


urlpatterns = [
    url(r'^signup/$', signup, name='signup'),
    url(r'^profile/$', profile, name='profile'),
]