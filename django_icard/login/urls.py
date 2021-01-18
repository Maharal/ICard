from django.conf.urls import url
from django_icard.login import views as core_views


urlpatterns = [
    url(r'^signup/$', core_views.signup, name='signup'),
]