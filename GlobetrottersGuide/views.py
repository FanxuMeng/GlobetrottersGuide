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
    context_dict = {}
    try:
        continent_list = Continent.objects.order_by('-likes')
        latest_review_list = Review.objects.order_by('-publish_date')[:5]
        context_dict['continents'] = continent_list
        context_dict['reviews'] =  latest_review_list
    except Continent.DoesNotExist:
        context_dict['continents'] = None
        context_dict['reviews'] = None
    return render(request, 'GlobetrottersGuide/home.html', context=context_dict)

def home_continent(request, continent_name_slug):
    context_dict = {}
    try:
        country_list = Country.objects.filter(Continent=continent_name_slug).order_by('-likes')[:10]
        review_list = Review.objects.order_by('-likes')[:5]
        context_dict['countries'] = country_list
        context_dict['reviews'] = review_list
    except Country.DoesNotExist:
        context_dict['countries'] = None
        context_dict['reviews'] = None
    return render(request, 'GlobetrottersGuide/home_continent.html', context=context_dict)

def home_country(request, country_name_slug):
    context_dict = {}
    try:
        city_list = City.objects.filter(Country=country_name_slug).order_by('-likes')[:10]
        review_list = Review.objects.order_by('-likes')[:5]
        context_dict['cities'] = city_list
        context_dict['reviews'] = review_list
    except City.DoesNotExist:
        context_dict['cities'] = None
        context_dict['reviews'] = None
    return render(request, 'GlobetrottersGuide/home_country.html', context=context_dict)

@login_required
def add_review(request, country_name_slug, city_name_slug):
    country = get_object_or_404(Country, pk=country_name_slug)
    city = get_object_or_404(City, pk=city_name_slug)

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            rating = form.cleaned_data['rating']
            text = form.cleaned_data['text']
            timeSpent = form.cleaned_data['timeSpent']

            username = request.user.username
            review = Review()
            review.belong_country = country
            review.belong_city = city
            review.rating = rating
            review.text = text
            review.time_spent = timeSpent
            review.publish_date = datetime.now()
            review.save()

            return redirect(reverse('GlobetrottersGuide:home',
                                    kwargs={'country_name_slug': country_name_slug,
                                            'city_name_slug': city_name_slug}))
        else:
            print(form.errors)

    return render(request,'GlobetrottersGuide/add_review.html')

def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'GlobetrottersGuide/review_detail.html', {'review': review})

def about(request):
    context_dict = {}
    context_dict['boldmessage'] = 'Authors: Autumn, Ethan, Fanxu, Miguel'

    response = render(request, 'GlobetrottersGuide/about.html', context=context_dict)
    return response

def showUserProfile(request):
    username = request.user.username
    user = UserProfile.objects.get(username=username)
    return render(request, 'GlobetrottersGuide/UserProfile.html', {"user": user})

def showLikes(request):
    username = request.user.username
    like = UserProfile.objects.get(username=username)
    template = 'GlobetrottersGuide/UserLiked.html'
    ctxDct = {'likes':like}
    return render(request,template,ctxDct)

def home_city(request, city_name_slug):
    review_list = Review.objects.filter(belong_city=city_name_slug)
    ctxDct = {'review_list': review_list}
    template = 'GlobetrottersGuide/home_city.html'
    return render(request,template, ctxDct)

