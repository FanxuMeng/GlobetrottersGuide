from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime

from GlobetrottersGuide.forms import countryReviewForm
from GlobetrottersGuide.forms import cityReviewForm
from GlobetrottersGuide.forms import UserForm
from GlobetrottersGuide.forms import UserProfileForm

from GlobetrottersGuide.models import UserProfile
from GlobetrottersGuide.models import countryReview,cityReview
from GlobetrottersGuide.models import Continent
from GlobetrottersGuide.models import Country
from GlobetrottersGuide.models import City


def home(request):
    context_dict = {}
    try:
        continent_list = Continent.objects.order_by('-likes')
        latest_review_list = countryReview.objects.order_by('-publish_date')[:5]
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
        review_list = countryReview.objects.order_by('-likes')[:5]
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
        review_list = cityReview.objects.order_by('-likes')[:5]
        context_dict['cities'] = city_list
        context_dict['reviews'] = review_list
    except City.DoesNotExist:
        context_dict['cities'] = None
        context_dict['reviews'] = None
    return render(request, 'GlobetrottersGuide/home_country.html', context=context_dict)

@login_required
def add_countryReview(request, country_name_slug):
    country = get_object_or_404(Country, pk=country_name_slug)

    if request.method == 'POST':
        form = countryReviewForm(request.POST)

        if form.is_valid():
            rating = form.cleaned_data['rating']
            text = form.cleaned_data['text']
            timeSpent = form.cleaned_data['timeSpent']

            username = request.user.username
            review = countryReview()
            review.belong_country = country
            review.rating = rating
            review.text = text
            review.time_spent = timeSpent
            review.publish_date = datetime.now()
            review.save()

            return redirect(reverse('GlobetrottersGuide:home',
                                    kwargs={'country_name_slug': country_name_slug}))
        else:
            print(form.errors)

    return render(request,'GlobetrottersGuide/add_review.html')


@login_required
def add_cityReview(request, city_name_slug):
    city = get_object_or_404(City, pk=city_name_slug)

    if request.method == 'POST':
        form = cityReviewForm(request.POST)

        if form.is_valid():
            rating = form.cleaned_data['rating']
            text = form.cleaned_data['text']
            timeSpent = form.cleaned_data['timeSpent']

            username = request.user.username
            review = cityReview()
            review.belong_city = city
            review.rating = rating
            review.text = text
            review.time_spent = timeSpent
            review.publish_date = datetime.now()
            review.save()

            return redirect(reverse('GlobetrottersGuide:home',
                                    kwargs={'city_name_slug': city_name_slug}))
        else:
            print(form.errors)

    return render(request,'GlobetrottersGuide/add_review.html')


def review_detail(request, countryReview_id):
    countryReview = get_object_or_404(countryReview, pk=countryReview_id)
    return render(request, 'GlobetrottersGuide/review_detail.html', {'review': countryReview})


def about(request):
    context_dict = {}
    context_dict['boldmessage'] = 'Authors: Autumn, Ethan, Fanxu, Miguel'

    response = render(request, 'GlobetrottersGuide/about.html', context=context_dict)
    return response


def showUserProfile(request):
    username = request.user.username
    user = UserProfile.objects.get(username=username)
    return render(request, 'GlobetrottersGuide/UserProfile.html', {"user": user})
    
### restructured showLikes and home_city to handle empty gets
def showLikes(request):

    template = 'GlobetrottersGuide/UserLiked.html' ### template
    ctxDct = {}

    try:
        username = request.user.username
        like = UserProfile.objects.get(username=username) ### still needs to be changed to appropriate object

        ctxDct['username'] = username
        ctxDct['likes'] = like

    except like.DoesNotExist: ### user can still exist, but not have anything liked
        ctxDct['username'] = username
        ctxDct['likes'] = None

    return render(request,template,ctxDct)


def home_city(request, city_name_slug):

    template = 'GlobetrottersGuide/home_city.html' ### template
    ctxDct = {}

    try:
        review_list = cityReview.objects.filter(belong_city=city_name_slug)
        ctxDct['Reviews'] = review_list
        
    except review_list.DoesNotExist:
        ctxDct['Reviews'] = None
    
    return render(request,template, ctxDct)
### user register, check if it works
### feel free to add to it if we need more elements 
### register doesn't take in an email address, don't know if were meant to but im just going off of the forms.py file

def register(request):
    template = "" ### <------- change this probably to "register.html"
    
    isUser = False

    if request.method == 'POST':
        userForm = UserForm(request.POST)
        userProfileForm = UserProfileForm(request.POST)

        if userForm.is_valid() and userProfileForm.is_valid():
            user = UserForm.save()
            user.set_password(user.password)
            user.save()

            profile = userProfileForm.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES: #if the user gives a profile picture
                profile.picture = request.FILES['picture']
            profile.save()

            if 'nationality' in request.FILES: # if the user provides their nationality
                profile.nationality = request.FILES['nationality']
            profile.save()

            isUser = True
        else:
            print(userForm.errors,UserProfileForm.errors)
    else:
        ## blank forms 
        userForm = UserForm()
        userProfileForm = UserProfileForm()

    ctxDct = {'userForm':userForm,'userProfileForm':userProfileForm,'isUser':isUser}

    return render(request,template,ctxDct)

