__author__ = 'abc'

from django.conf.urls import url
from .import views

urlpatterns=[
    url(r'^location$', views.distance, name='distance'),
    url(r'^signUp$', views.createUser, name='createUser'),
    url(r'^signIn$', views.loginUser, name='loginUser'),
    url(r'^addLocation$', views.addLocation ,name='add'),
     url(r'^showAll$', views.distance,name='all'),
	url(r'^nearbyUsers$', views.nearbyUsers,name='nearby'),


]