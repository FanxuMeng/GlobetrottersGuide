#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path
from GlobetrottersGuide import views

app_name = 'GlobetrottersGuide'

urlpatterns = [
    path('',views.home, name='HomePage'),
    path('about/',views.about, name='about'),

    path('user/<int:user_id>/',
         views.showUserProfile, name='UserProfile'),
    path('user/<int:user_id>/likes/',
         views.showLikes, name='UserLiked'),

    path('<slug:continent_name_slug>/',
         views.home_continent, name='Home'),
    path('<slug:continent_name_slug>/<slug:country_name_slug>/',
         views.home_country, name='Country'),
    path('<slug:continent_name_slug>/<slug:country_name_slug>/<slug:city_name_slug>/',
         views.home_city, name='City'),
    path('writeCountryReview/',
         views.add_countryReview, name='Reviewing'),
    path('writeCityReview/',
         views.add_cityReview, name='Reviewing'),
    path('<slug:continent_name_slug>/<slug:country_name_slug>/<int:cityReview_id>/',
         views.review_detail, name='review'),
    path('<slug:continent_name_slug>/<int:countryReview_id>/',
         views.review_detail, name='review'),
]