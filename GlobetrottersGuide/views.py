from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime

from GlobetrottersGuide.forms import ReviewForm

from GlobetrottersGuide.models import UserProfile
from GlobetrottersGuide.models import Review
from GlobetrottersGuide.models import Continent
from GlobetrottersGuide.models import Country
from GlobetrottersGuide.models import City


def home(request):
    continent_list = Continent.objects.order_by('-likes')
    latest_review_list = Review.objects.order_by('-publish_date')[:5]

    context_dict = {}
    context_dict['continents'] = continent_list
    context_dict['reviews'] =  latest_review_list
    return render(request, '', context=context_dict)

def home_continent(request):
    country_list = Country.objects.order_by('-likes')[:10]
    review_list = Review.objects.order_by('-likes')[:5]

    context_dict = {}
    context_dict['countries'] = country_list
    context_dict['reviews'] = review_list
    return render(request, '', context=context_dict)

def home_country(request, country_name_slug):
    city_list = City.objects.order_by('-likes')[:10]
    review_list = Review.objects.order_by('-likes')[:5]

    context_dict = {}
    context_dict['cities'] = city_list
    context_dict['reviews'] = review_list
    return render(request, '', context=context_dict)

@login_required
def add_review(request, country_name_slug, city_name_slug):
    country = get_object_or_404(Country, pk=country_name_slug)
    city = get_object_or_404(City, pk=city_name_slug)
    '''
    try:
        country = Country.objects.get(slug=country_name_slug)
    except Country.DoesNotExist:
        country = None

    try:
        city = City.objects.get(name=city_name_slug)
    except City.DoesNotExist:
        city = None
    '''

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            rating = form.cleaned_data['rating']



    return render(request, '', context)


def showUserProfile(request, username):
    user = UserProfile.objects.get(username=username)
    return render(request, '', {"user":user})

    #The blank '' will eventually be GlobetrottersGuide/user_profile.html when the template is finished
#def showLikes(request):
#def showreview(requset):
