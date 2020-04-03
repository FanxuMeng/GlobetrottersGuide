#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Fanxu Meng
# All rights reserved (C) 2019 by Fanxu Meng

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
'GlobetrottersGuide_project.settings')

import django
django.setup()
from GlobetrottersGuide.models import Continent, Country, City, User, UserProfile, cityReview, countryReview
from datetime import timedelta

def populate():
    canada_city = ['Ottawa','Edmonton','Toronto']
    usa_cities = ['New York', 'Los Angeles', 'Chicago', 'San Francisco']
    cn_cities = ['Beijing', 'Shanghai', 'Guangzhou', 'Chongqing','Hong Kong','Taipei']
    jp_cities = ['Tokyo', 'Osaka', 'Kyoto']

    continent_dic = {'Asia':{'Japan':jp_cities,'China':cn_cities},
                     'North America':{'America':usa_cities,'Canada':canada_city}}

    for continent, country in continent_dic.items():
        a = add_continent(continent)
        for b, city_list in country.items():
            c1 = add_country(a, b)
            for c in city_list:
                add_city(c1, c)
    
    user = User.objects.get(username="gtg")
    date =  "2015-04-06T20:38:59Z"
    time = timedelta(days=4)
    city = City.objects.get(name="Los Angeles")
    add_cityReview(city,user,date,35,14,time,5, "Small town America is like nothing you’ve ever seen until you visit one of the close-knit communities which abound in the more rural areas. Friendly and with a welcoming attitude, it’s hard not to feel at home!")
    date =  "2017-05-02T20:38:59Z"
    time = timedelta(days=10)
    city = City.objects.get(name="New York")
    add_cityReview(city,user,date,80,54,time,1, "I would not recommend - New York's major social problems include poverty, crime and drug addiction, and racial conflict. Poverty is one of New York City's most expensive problems.")
    date =  "2020-04-03T20:38:59Z"
    time = timedelta(days=2)
    country = Country.objects.get(name="Canada")
    add_countryReview(country,user,date,115,81,time,4, "Canada is big and beautiful. All 9.98 million square kilometres of it. As the second largest country in the world, Canada boasts endless lakes and rivers. We have access to three oceans, and we boast one of the few places in the world you can ski and surf (outside) in the same day.")
    date =  "2019-01-09T20:38:59Z"
    time = timedelta(days=13)
    country = Country.objects.get(name="China")
    add_countryReview(country,user,date,70,11,time,2, "A visit to the world’s largest palace complex is forbidden no more; in fact, for many tourists, a trip to this rambling fortress is one of Beijing’s numerous highlights. Off limits for nearly 500 years, the Forbidden City was home to two reclusive dynasties between 1420 and 1912, but today everyone can enjoy the imperial architecture and art of this Unesco World Heritage Site.")

def add_continent(name):
    a = Continent.objects.get_or_create(name=name)[0]
    a.likes = 0
    a.save()
    return a

def add_country(continent, name):
    b = Country.objects.get_or_create(continent=continent,name=name)[0]
    b.likes = 0
    b.views = 0
    b.save()
    return b

def add_city(country, name):
    c = City.objects.get_or_create(country=country,name=name)[0]
    c.likes = 0
    c.views = 0
    c.save()
    return c

def add_cityReview(city, user, date, view, like, time, rating, text):
    d, created = cityReview.objects.get_or_create(user=user,belong_city=city,publish_date=date,views=view,likes=like,timeSpent=time,rating=rating,text=text)
    d.save()
    return d

def add_countryReview(country, user, date, view, like, time, rating, text):
    d, created = countryReview.objects.get_or_create(user=user,belong_country=country,publish_date=date,views=view,likes=like,timeSpent=time,rating=rating,text=text)
    d.save()
    return d

if __name__ == '__main__':
    print('Starting GlobetrottersGuide population script...')
    populate()
