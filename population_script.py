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

    city = City.objects.get(name="Los Angeles")
    date =  "2015-04-06T20:38:59Z"
    add_cityReview(city,user,date,35,14,timedelta(days=4),5,"Loved.", "Small town America is like nothing you’ve ever seen until you visit one of the close-knit communities which abound in the more rural areas. Friendly and with a welcoming attitude, it’s hard not to feel at home!")
    date =  "2019-05-03T20:38:59Z"
    add_cityReview(city,user,date,50,7,timedelta(days=7),3,"Friendly People", "It’s true when people say that Americans are particularly friendly. They’re less formal than Brits and they do have a knack of making newcomers feel right at home.")
    date =  "2016-03-01T20:38:59Z"
    add_cityReview(city,user,date,112,56,timedelta(days=5),4,"Vacations are good", "We’re not just talking about vacations here. “Holiday” in America means everything from Halloween Trick or Treat and Thanksgiving dinner to Christmas and they celebrate big time in the USA! Take a look at the Fourth of July fireworks…")
    date =  "2017-02-02T20:38:59Z"
    add_cityReview(city,user,date,52,7,timedelta(days=9),3,"Ok.", "Malls in America are a key part of modern American culture and are like cities within cities. The country has some of the most incredible shopping experiences on the planet.")
    
    city = City.objects.get(name="New York")
    date =  "2017-05-03T20:38:59Z"
    add_cityReview(city,user,date,67,23,timedelta(days=10),1,"Never", "I would not recommend - New York's major social problems include poverty, crime and drug addiction, and racial conflict. Poverty is one of New York City's most expensive problems.")
    date =  "2018-03-05T20:38:59Z"
    add_cityReview(city,user,date,76,14,timedelta(days=16),4,"Wow.", "The glamour of America is not just at the Oscars – it’s visible in every fashion outlet, every nail bar, every nightclub and every hotel. Americans adore glitz and glamour and you can be part of it too!")
    date =  "2020-01-02T20:38:59Z"
    add_cityReview(city,user,date,52,12,timedelta(days=1),3,"So creative.", "An innovative, creative and exciting music scene has always been a big part of the country that invented rock and roll, country and western, grunge and the modern musical. Lots to enjoy for the music lovers out there!")
    
    city = City.objects.get(name="Chicago")
    date =  "2017-05-02T20:38:59Z"
    add_cityReview(city,user,date,321,199,timedelta(days=10),5,"Great", "Chicago has worked hard to make sure things are easy to get to. There’s a store on every corner and public transport is generally excellent.")
    date =  "2018-03-03T20:38:59Z"
    add_cityReview(city,user,date,91,23,timedelta(days=16),4,"Wonderful", "Hugely diverse in terms of its population, America is home to the traveller. You’ll benefit from the wonderful mixture of the Hispanic, Latino, Asian and European influences which have built up this country to be what it is today.")

    city = City.objects.get(name="Toronto")
    date =  "2019-02-02T20:38:59Z"
    add_cityReview(city,user,date,80,34,timedelta(days=8),5,"Amazing", "Canada's most populous city has a lot to offer in terms of activities and culture. From the famous CN Tower to the Royal Ontario Museum, you'll never be bored.")
    date =  "2020-03-11T20:38:59Z"
    add_cityReview(city,user,date,98,52,timedelta(days=3),4,"Great", "Toronto is home to some 2.7 million people, a sprawling city filled with distinct shouldering neighbourhoods.")
    date =  "2020-01-09T20:38:59Z"
    add_cityReview(city,user,date,34,14,timedelta(days=9),3,"Ok.", "Most of us will have heard of the Toronto Film Festival, but the city is also host to a whole summer of boutique alternative dance and electronic festivals - including Digital Dreams, Electric Island and Diplo’s annual Mad Decent Block Party. Arts lovers will want to travel over in June, when a 17-day festival, Luminato, will take over the Toronto's theatres, parks and public spaces with theatre, dance and music.")
    date =  "2020-01-02T20:38:59Z"
    add_cityReview(city,user,date,56,54,timedelta(days=6),4,"Amazing", "As well as a good deal of major art museums: the Art Gallery of Ontario, Toronto Gallery of Inuit Arts and the Gardiner Museum of Ceramic art, the city has a burgeoning art community that’s present in every corner. ")

    city = City.objects.get(name="Ottawa")
    date =  "2020-02-26T20:38:59Z"
    add_cityReview(city,user,date,176,132,timedelta(days=10),5,"Super", "Ice skating along the Rideau Canal Skateway is a beloved local pastime. It’s also about the most fun way to tour Canada’s capital on holiday. At nearly eight kilometres, it’s considered the world’s largest rink. Warm up with hot cocoa from on-ice shops or try classic Canadian snacks like a Beavertail pastry or a poutine— french fries smothered in gravy and cheese curds.")
    date =  "2019-01-18T20:38:59Z"
    add_cityReview(city,user,date,165,122,timedelta(days=16),4,"Good", "You can spend hours picking up local produce and fresh fish, and browsing the boutiques, stalls, and cafés of open-air ByWard Market, Canada’s oldest continuously-operating farmers' market. In Lower Town, it’s bordered by George, York, ByWard and Williams Streets. The brick buildings are quaint and the place is always bustling. Make time for people-watching.")

    city = City.objects.get(name="Shanghai")
    date =  "2016-03-20T20:38:59Z"
    add_cityReview(city,user,date,102,81,timedelta(days=3),5,"Great", "The record-breaking high-rise buildings form a futuristic skyline in Shanghai, while the advanced high-speed railway, metro lines, and world’s fastest maglev train also make traveling the city cutting-edge quick. It can be said that Shanghai is a window to modern China.")
    date =  "2017-09-15T20:38:59Z"
    add_cityReview(city,user,date,84,100,timedelta(days=19),3,"Meh", "Shanghai was one of the earliest open ports in China, experienced a colonial history during the two world wars, and was a shelter for Russian and Jewish refugees during these times of warfare. Today, the turbulent history still leaves deep imprints and inspiring stories about the city.")
    
    city = City.objects.get(name="Hong Kong")
    date =  "2017-08-18T20:38:59Z"
    add_cityReview(city,user,date,78,63,timedelta(days=3),5,"Ok", "The best part about traveling to Hong Kong with your family is that Hong Kong is home to the famous Disneyland Park, and the Ocean Park. At Disneyland, your child will have a blast of a time playing with their favourite Disney characters, and at Ocean Park, you get to learn about the sea animals and also get to see the adorable panda named Jia-Jia, as well as the very rare Red Panda.")
    date =  "2020-04-16T20:38:59Z"
    add_cityReview(city,user,date,27,12,timedelta(days=4),3,"Fine", "One of the things to know when visiting Hong Kong, is that it’s not all skyscrapers and tall buildings. Not many people are aware of the fact that the skyscrapers only occupy one-third of the territory, and the rest of Hong Kong is full of beautiful mountains, enchanting forests and pristine beaches.")

    city = City.objects.get(name="Beijing")
    date =  "2020-03-07T20:38:59Z"
    add_cityReview(city,user,date,65,23,timedelta(days=2),1,"Great", "Most of Beijing’s hutong districts have, alas, been swept away by the tide of progress, demolished to make way for new roads and shiny skyscrapers.")
    date =  "2019-04-30T20:38:59Z"
    add_cityReview(city,user,date,78,45,timedelta(days=7),4,"Good", "China’s ceaseless censorship tsars work overtime to stop its citizens learning about the 1989 Tiananmen Square massacre, when government troops brutally supressed a pro-democracy rally, leaving scores dead. Feel the weight of history with a visit to the square, where the “Tank Man” famously stood in front of a column of tanks the day after the massacre.")
    date =  "2018-03-20T20:38:59Z"
    add_cityReview(city,user,date,88,34,timedelta(days=4),4,"Fine", "Taking tea is a time-honoured tradition in China and for travellers wedded to a builder’s brew, Beijing’s bountiful infusions could provide grounds for divorce. There’s a tea for every occasion in the city – green tea, gunpowder tea, golden monkey tea and jasmine tea, to name a few – and the best place to sample them is Maliandao Tea Market, where some 900 vendors ply their leafy trade.")
    date =  "2019-02-21T20:38:59Z"
    add_cityReview(city,user,date,76,32,timedelta(days=6),4,"Great", "Most of us know a Chinese restaurant that does a decent Peking duck, but for the genuine article you really need to visit Beijing, formerly Peking, which invented the dish.")
    
    city = City.objects.get(name="Tokyo")
    date =  "2015-07-20T20:38:59Z"
    add_cityReview(city,user,date,134,86,timedelta(days=3),1,"Anxious", "The food in Tokyo is fresh, rich, and delicious, and the sheer amount of options is overwhelming to me.")
    date =  "2018-03-15T20:38:59Z"
    add_cityReview(city,user,date,234,200,timedelta(days=19),4,"Great", "The Roppongi Hills Mori Tower is a 54-story high skyscraper that houses companies like Google Japan, Pokemon, and The Mori Art Museum. The gorgeous observation deck offers a breathtaking 360-degree view of the city skyline.")

    city = City.objects.get(name="Kyoto")
    date =  "2020-01-26T20:38:59Z"
    add_cityReview(city,user,date,154,32,timedelta(days=2),5,"Great", "If you can go only one place in Japan to see the cherry blossoms, make it Kyoto, the city that inspired the term hanami, or flower viewing party.")
    date =  "2018-06-21T20:38:59Z"
    add_cityReview(city,user,date,198,103,timedelta(days=6),2,"Don't", "Experience the world-famous Japanese hospitality known as omotenashi at some of the best ryokan in all of Japan, which range from the budget to the very high-end.")
    
    date =  "2020-04-03T20:38:59Z"
    time = timedelta(days=2)
    country = Country.objects.get(name="Canada")
    add_countryReview(country,user,date,115,81,time,4,"Great", "Canada is big and beautiful. All 9.98 million square kilometres of it. As the second largest country in the world, Canada boasts endless lakes and rivers. We have access to three oceans, and we boast one of the few places in the world you can ski and surf (outside) in the same day.")
    date =  "2019-01-09T20:38:59Z"
    time = timedelta(days=13)
    country = Country.objects.get(name="China")
    add_countryReview(country,user,date,70,11,time,2,"Fine", "A visit to the world’s largest palace complex is forbidden no more; in fact, for many tourists, a trip to this rambling fortress is one of Beijing’s numerous highlights. Off limits for nearly 500 years, the Forbidden City was home to two reclusive dynasties between 1420 and 1912, but today everyone can enjoy the imperial architecture and art of this Unesco World Heritage Site.")
    date =  "2020-04-01T20:38:59Z"
    time = timedelta(days=5)
    country = Country.objects.get(name="America")
    add_countryReview(country,user,date,1033,721,time,4,"Good", "From Hollywood to Broadway, America leads the way in movies and musicals. So whether you’re just looking for the best in entertainment or want to progress your career, this is the place you need to be.")



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

def add_cityReview(city, user, date, view, like, time, rating, title, text):
    d, created = cityReview.objects.get_or_create(user=user,belong_city=city,publish_date=date,views=view,likes=like,timeSpent=time,rating=rating,title=title,text=text)
    d.save()
    return d

def add_countryReview(country, user, date, view, like, time, rating, title, text):
    d, created = countryReview.objects.get_or_create(user=user,belong_country=country,publish_date=date,views=view,likes=like,timeSpent=time,rating=rating,title=title,text=text)
    d.save()
    return d

if __name__ == '__main__':
    print('Starting GlobetrottersGuide population script...')
    populate()
