#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path
from GlobetrottersGuide import views

app_name = 'GlobetrottersGuide'

urlpatterns = [
    path('',views.home, name='HomePage'),
    path('about/',views.about, name='about'),

    path('user/<username>/',
         views.showUserProfile, name='UserProfile'),

    path('user/<username>/editProfile/', views.editProfile, name='EditProfile'),

    path('<slug:continent_name_slug>/',
         views.home_continent, name='continent'),

    path('<slug:continent_name_slug>/<slug:country_name_slug>/',
         views.home_country, name='country'),

    path('<slug:continent_name_slug>/<slug:country_name_slug>/<slug:city_name_slug>/',
         views.home_city, name='city'),

    path('<slug:continent_name_slug>/<slug:country_name_slug>/writeCountryReview/',
         views.add_countryReview, name='ReviewCountry'),
    path('<slug:continent_name_slug>/<slug:country_name_slug>/<slug:city_name_slug>/writeCityReview/',
         views.add_cityReview, name='ReviewCity'),
    path('<slug:continent_name_slug>/<slug:country_name_slug>/<slug:city_name_slug>/<int:cityReview_id>/',
         views.cityReview_detail, name='review'),
    path('<slug:continent_name_slug>/<slug:country_name_slug>/<int:countryReview_id>/',
         views.countryReview_detail, name='review'),
]