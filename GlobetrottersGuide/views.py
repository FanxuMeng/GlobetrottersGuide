from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.views import View

from GlobetrottersGuide.forms import countryReviewForm
from GlobetrottersGuide.forms import cityReviewForm
from GlobetrottersGuide.forms import EditProfileForm

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
    context_dict['continent_slug'] = Continent.objects.get(slug=continent_name_slug).slug
    context_dict['continent_name'] = Continent.objects.get(slug=continent_name_slug).name
    try:
        country_list = []
        for country in Country.objects.all():
            if country.getContinentSlug() == continent_name_slug:
                country_list.append(country)

        review_list = []
        for review in countryReview.objects.all():
            if review.belong_country.getContinentSlug() == continent_name_slug:
                review_list.append(review)
        for review in cityReview.objects.all():
            if review.belong_city.country.getContinentSlug() == continent_name_slug:
                review_list.append(review)

        context_dict['countries'] = country_list
        context_dict['reviews'] = review_list[:5]
    except Country.DoesNotExist:
        context_dict['countries'] = None
        context_dict['reviews'] = None

    return render(request, 'GlobetrottersGuide/home_continent.html', context=context_dict)

def home_country(request,continent_name_slug, country_name_slug):
    context_dict = {}
    country = Country.objects.get(slug=country_name_slug)
    context_dict['continent_slug'] = Continent.objects.get(slug=continent_name_slug).slug
    context_dict['country_slug'] = country.slug
    context_dict['country_name'] = country.name
    try:
        city_list = []
        for city in City.objects.all():
            if city.getCountrySlug() == country_name_slug:
                city_list.append(city)

        review_list = []
        for review in countryReview.objects.all():
            if review.belong_country.slug == country_name_slug:
                review_list.append(review)
        for review in cityReview.objects.all():
            if review.belong_city.getCountrySlug() == country_name_slug:
                review_list.append(review)

        context_dict['cities'] = city_list
        context_dict['reviews'] = review_list[:5]
    except City.DoesNotExist:
        context_dict['cities'] = None
        context_dict['reviews'] = None
    return render(request, 'GlobetrottersGuide/home_country.html', context=context_dict)


def home_city(request,continent_name_slug, country_name_slug, city_name_slug):
    context_dict = {}
    country = Country.objects.get(slug=country_name_slug)
    city = City.objects.get(slug=city_name_slug)
    context_dict['country_slug'] = country.slug
    context_dict['country_name'] = country.name
    context_dict['city_name'] = city.name

    try:
        review_list = []
        for review in cityReview.objects.all():
            if review.belong_city.slug == city_name_slug:
                review_list.append(review)

        context_dict['reviews'] = review_list
        context_dict['review_num'] = len(review_list)
        
    except review_list.DoesNotExist:
        context_dict['reviews'] = None
    
    return render(request,'GlobetrottersGuide/home_city.html', context_dict)

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

    context_dict = {}
    context_dict['userProfile'] = user
    try:
        countryReview_list = countryReview.objects.get(username=username)
        context_dict['countryReview'] = countryReview_list
    except countryReview.DoesNotExist:
        context_dict['countryReview'] = None

    try:
        cityReview_list = cityReview.objects.get(username=username)
        context_dict['cityReview'] = cityReview_list
    except cityReview.DoesNotExist:
        context_dict['cityReview'] = None

    return render(request, 'GlobetrottersGuide/UserProfile.html', context=context_dict)

def editProfile(request):
    user = request.user
    form = EditProfileForm(request.POST or None, initial={'username':user.username, 'nationality':user.nationality})
    if request.method == 'POST':
        if form.is_valid():

            user.nationality = request.POST['nationality']
            user.username = request.POST['username']

            user.save()
            
            
            return HttpResponseRedirect('%s'%(reverse('profile')))
        
    
    return render(request, 'GlobetrottersGuide/editProfile.html', {"form": form})
    
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
### get lists for search suggestions
def getContinentList(maxResults=0, startsWith=''):
    continentList = []

    if startsWith:
        continentList = Continent.objects.filter(name__isstartswith=startsWith)
    if maxResults > 0:
        if len(continentList)>maxResults:
            continentList = continentList[:maxResults]
    return continentList

def getCityList(maxResults=0, startsWith=''):
    cityList = []

    if startsWith:
        cityList = City.objects.filter(name__isstartswith=startsWith)
    if maxResults > 0:
        if len(cityList)>maxResults:
            cityList = cityList[:maxResults]
    return cityList

def getCountryList(maxResults=0, startsWith=''):
    countryList = []

    if startsWith:
        countryList = Country.objects.filter(name__isstartswith=startsWith)
    if maxResults > 0:
        if len(countryList)>maxResults:
            countryList = countryList[:maxResults]
    return countryList
## throw out some search suggestions
class suggestionView(View):
    def get(self,request):
        theList = []
        loopOut = False
        notContinent = True
        notCountry = True
        notCity = True
        if 'suggestion' in request.GET:
            suggestion = request.GET['suggestion']
        else:
            suggestion = ''

        while(loopOut==False):
            theList = getContinentList(5,suggestion)
            template = "continents.html" ##change this
            ctxDct = {'Continents': theList}
            theList = Continent.objects.order_by('-name')
            notContinent = False
            loopOut = True
            if len(theList) == 0 and notContinent == True:
                theList = getCountryList(4,suggestion)
                template = "country.html" ##change this
                ctxDct = {'Countries': theList}
                theList = Country.objects.order_by('-name')
                notCountry = False
                loopOut = True
            elif len(theList) == 0 and notContinent == True and notCountry == True:
                theList = getCityList(4,suggestion)
                template = "city.html" ##change this
                ctxDct = {'City':theList}
                theList = City.objects.order_by('-name')
                notCity = False
                loopOut = True
            elif len(theList) == 0 and notContinent == True and notCountry == True and notCity == True:
                theList = []
                ctxDct = {}
                template = ""## whatever
                loopOut = True

        return render(request,template,ctxDct)
            


