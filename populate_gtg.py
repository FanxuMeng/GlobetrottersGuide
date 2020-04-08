#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Fanxu Meng
# All rights reserved (C) 2019 by Fanxu Meng

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
'GlobetrottersGuide_project.settings')

import django
django.setup()
from GlobetrottersGuide.models import Continent, Country, City

def populate():
    canada_city = ['Ottawa','Edmonton','Toronto']
    usa_cities = ['New York', 'Los Angeles', 'Chicago', 'San Francisco']
    cn_cities = ['Beijing', 'Shanghai', 'Guangzhou', 'Chongqing','Hong Kong','Taipei']
    jp_cities = ['Tokyo', 'Osaka', 'Kyoto']

    continent_dic = {'Asia':{'Japan':jp_cities,'China':cn_cities},
                     'North America':{'America':usa_cities,'Canada':canada_city},
                     'Africa':{},
                     'Antarctica':{},
                     'Europe':{},
                     'Oceania':{},
                     'South America':{},
                     }

    for continent, country in continent_dic.items():
        a = add_continent(continent)
        for b, city_list in country.items():
            c1 = add_country(a, b)
            for c in city_list:
                add_city(c1, c)

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

if __name__ == '__main__':
    print('Starting GlobetrottersGuide population script...')
    populate()
