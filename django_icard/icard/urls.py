"""icard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic.base import TemplateView, RedirectView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #url(r'^$', views.home_page, name='home'),
    #url(r'^login/$', views.login, name='login'),
    #url(r'^signup/$', views.signup, name='signup'),
    path('admin/', admin.site.urls),
    path('cards/', include('cards.urls')),
    path('cards/', include('django.contrib.auth.urls')),
    path('getAllCards/', TemplateView.as_view(template_name='home.html'), name='get_all_cards'),
    path('newCard/', TemplateView.as_view(template_name='new_card.html'), name='get_card'),
    path('', RedirectView.as_view(url='/cards', permanent=False), name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)