from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime

from GlobetrottersGuide.forms import countryReviewForm, EditProfileForm
from GlobetrottersGuide.forms import cityReviewForm

from django.contrib.auth.models import User
from GlobetrottersGuide.models import UserProfile
from GlobetrottersGuide.models import countryReview, cityReview
from GlobetrottersGuide.models import Continent
from GlobetrottersGuide.models import Country
from GlobetrottersGuide.models import City


@login_required(login_url='accounts/login')
def pass_userProfile(request, username):
    user = User.objects.get(username=username)
    context_dict = {}
    try:
        userProfile = UserProfile.objects.get(user=user)
        context_dict['userProfile'] = userProfile
    except UserProfile.DoesNotExist:
        context_dict['userProfile'] = None
    return render(request, 'GlobetrottersGuide/base.html', context=context_dict)


def home(request):
    context_dict = {}
    try:
        continent_list = Continent.objects.order_by('-likes')
        country_review_list = countryReview.objects.order_by('-publish_date')[:3]
        city_review_list = cityReview.objects.order_by('-publish_date')[:3]
        context_dict['continents'] = continent_list
        context_dict['country_reviews'] = country_review_list
        context_dict['city_reviews'] = city_review_list

        for continent in continent_list:
            continent.reviewNum = getContinentReviewNum(continent.slug)
        
    except Continent.DoesNotExist:
        context_dict['continents'] = None
        context_dict['country_reviews'] = None
        context_dict['city_reviews'] = None
    return render(request, 'GlobetrottersGuide/home.html', context=context_dict)


def home_continent(request,continent_name_slug):
    context_dict = {}
    try:
        continent = Continent.objects.get(slug=continent_name_slug)
        country_list = Country.objects.filter(continent=continent).order_by('-views')[:10]
        country_review_list = countryReview.objects.filter(belong_country__continent=continent).order_by('-publish_date')
        city_review_list = cityReview.objects.filter(belong_city__country__continent=continent).order_by('-publish_date')
        context_dict['continent'] = continent
        context_dict['countries'] = country_list
        context_dict['country_reviews'] = country_review_list
        context_dict['city_reviews'] = city_review_list
    except Country.DoesNotExist:
        context_dict['countries'] = None
        context_dict['reviews'] = None
    
    for country in country_list:
            country.reviewNum = getCountryReviewNum(country.slug)

    return render(request, 'GlobetrottersGuide/home_continent.html', context=context_dict)


def home_country(request, continent_name_slug, country_name_slug):
    context_dict = {}
    try:
        continent = Continent.objects.get(slug=continent_name_slug)
        country = Country.objects.get(slug=country_name_slug)
        city_list = City.objects.filter(country=country).order_by('-views')[:10]
        review_list = countryReview.objects.filter(belong_country=country).order_by('-publish_date')
        context_dict['continent'] = continent
        context_dict['country'] = country
        context_dict['cities'] = city_list
        context_dict['reviews'] = review_list
    except City.DoesNotExist:
        context_dict['cities'] = None
        context_dict['reviews'] = None

    for city in city_list:
            city.reviewNum = getCityReviewNum(city.slug)

    return render(request, 'GlobetrottersGuide/home_country.html', context=context_dict)


def home_city(request, continent_name_slug, country_name_slug, city_name_slug):
    context_dict = {}
    try:
        continent = Continent.objects.get(slug=continent_name_slug)
        country = Country.objects.get(slug=country_name_slug)
        city = City.objects.get(slug=city_name_slug)
        reviews = cityReview.objects.filter(belong_city=city).order_by('-publish_date')
        context_dict['continent'] = continent
        context_dict['country'] = country
        context_dict['city'] = city
        context_dict['reviews'] = reviews
        context_dict['review_num'] = len(reviews)
    except City.DoesNotExist:
        context_dict['city'] = None

    return render(request, 'GlobetrottersGuide/home_city.html', context=context_dict)

def getContinentReviewNum(continent_slug):
    count = 0
    for review in cityReview.objects.all():
        if review.belong_city.getCountry().getContinentSlug() == continent_slug:
            count+=1
    for review in countryReview.objects.all():
        if review.belong_country.getContinentSlug() == continent_slug:
            count+=1
    return count       

def getCountryReviewNum(country_slug):
    count = 0
    for review in cityReview.objects.all():
        if review.belong_city.getCountrySlug() == country_slug:
            count+=1
    for review in countryReview.objects.all():
        if review.belong_country.slug == country_slug:
            count+=1
    return count     

def getCityReviewNum(city_slug):
    count = 0
    for review in cityReview.objects.all():
        if review.belong_city.slug == city_slug:
            count+=1
    return count      


@login_required(login_url='accounts/login')
def add_countryReview(request, continent_name_slug, country_name_slug):
    context_dict = {}
    try:
        continent = Continent.objects.get(slug=continent_name_slug)
        country = Country.objects.get(slug=country_name_slug)
        context_dict['continent'] = continent
        context_dict['country'] = country
    except Country.DoesNotExist:
        context_dict['country'] = None

    if context_dict['country'] is None:
        return redirect('GlobetrottersGuide:HomePage')

    form_class = countryReviewForm
    form = form_class(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():
            if country:
                user = request.user
                review = countryReview()
                review.belong_country = country
                review.user = user
                review.publish_date = datetime.now()
                review.save()

                return redirect(reverse('GlobetrottersGuide:home_country',
                                        kwargs={'continent_name_slug': continent_name_slug,
                                                'country_name_slug': country_name_slug}))
        else:
            print(form.errors)

    context_dict['form'] = form
    return render(request, 'GlobetrottersGuide/add_countryReview.html', context=context_dict)


@login_required(login_url='accounts/login')
def add_cityReview(request, continent_name_slug, country_name_slug, city_name_slug):
    context_dict = {}
    try:
        continent = Continent.objects.get(slug=continent_name_slug)
        country = Country.objects.get(slug=country_name_slug)
        city = City.objects.get(slug=city_name_slug)
        context_dict['continent'] = continent
        context_dict['country'] = country
        context_dict['city'] = city
    except City.DoesNotExist:
        context_dict['city'] = None

    if context_dict['city'] is None:
        return redirect('GlobetrottersGuide:HomePage')

    form_class = cityReviewForm
    form = form_class(request.POST)

    if request.method == 'POST':

        if form.is_valid():
            if city:
                user = request.user
                review = cityReview()
                review.user = user
                review.belong_city = city
                review.publish_date = datetime.now()
                review.save()

                return redirect(reverse('GlobetrottersGuide:home_city',
                                        kwargs={'continent_name_slug': continent_name_slug,
                                                'country_name_slug': country_name_slug,
                                                'city_name_slug': city_name_slug}))
        else:
            print(form.errors)

    context_dict['form'] = form
    return render(request,'GlobetrottersGuide/add_cityReview.html', context=context_dict)


def about(request):
    context_dict = {}
    context_dict['organization'] = "University of Glasgow"
    context_dict['authors'] = 'Authors: Autumn, Ethan, Fanxu, Miguel'
    response = render(request, 'GlobetrottersGuide/about.html', context=context_dict)
    return response


def showUserProfile(request, username):
    context_dict = {}
    user = User.objects.get(username=username)
    context_dict['user'] = user
    try:
        userProfile = UserProfile.objects.get(user=user)
        context_dict['userProfile'] = userProfile
    except UserProfile.DoesNotExist:
        return redirect(reverse('GlobetrottersGuide:EditProfile',
                                kwargs={'username': user.username}))

    try:
        countryReview_list = countryReview.objects.filter(user=user)
        context_dict['country_reviews'] = countryReview_list
    except countryReview.DoesNotExist:
        context_dict['country_reviews'] = None

    try:
        cityReview_list = cityReview.objects.filter(user=user)
        context_dict['city_reviews'] = cityReview_list
    except cityReview.DoesNotExist:
        context_dict['city_reviews'] = None

    return render(request, 'GlobetrottersGuide/UserProfile.html', context=context_dict)


@login_required(login_url='accounts/login')
def editProfile(request, username):
    user = User.objects.get(username=username)
    form = EditProfileForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            userProfile = UserProfile()
            user.Email = request.POST['email']
            userProfile.picture = request.POST['picture']
            userProfile.nationality = request.POST['nationality']

            userProfile.save()
            user.save()

            return HttpResponseRedirect('%s' % (reverse('profile')))

    return render(request, 'GlobetrottersGuide/editProfile.html', {"form": form})

