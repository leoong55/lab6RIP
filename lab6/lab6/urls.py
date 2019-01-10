"""Templating URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^function_view/', views.function_view),
    #url(r'^class_based_view/', views.ExampleClassBase.as_view()),
    url(r'^$', views.ExampleView.as_view(), name='start'),
    url(r'^bullets/', views.BulletsView.as_view()),
    url(r'^bullet/(?P<id>\d+)', views.BulletView.as_view(), name='bullet_url'),
    url(r'^signupold/', views.registration_old, name='signupNOFORM'),
    url(r'^signup/', views.registration, name='signup'),
    url(r'^login/', views.authorization, name='login'),
    url(r'^logout/', views.exit, name='logout'),
]

