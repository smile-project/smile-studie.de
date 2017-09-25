from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_site, name='home'),
    url(r'privacy', views.privacy_site, name='privacy')
]