from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime

from GlobetrottersGuide.models import UserProfile
from GlobetrottersGuide.models import Review
from GlobetrottersGuide.models import Continent
from GlobetrottersGuide.models import Country
from GlobetrottersGuide.models import City


def home(request):
    request.session.set_test_cookie()


def showUserProfile(request):


def showLikes(request):



def writereview(request):


def showreview(requset):


