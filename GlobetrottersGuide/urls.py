#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path
from GlobetrottersGuide import views

app_name = 'GlobetrottersGuide'

urlpatterns = [
    path('',views.home, name='HomePage'),
    path('about/',views.about, name='about'),
    ###path('register/',views.register,name='register') ###commented out until register gets finished
]