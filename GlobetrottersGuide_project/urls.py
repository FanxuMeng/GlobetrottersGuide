"""GlobetrottersGuide_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from GlobetrottersGuide import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('GlobetrottersGuide.urls')),

    path('myprofile/',views.showUserProfile, name='MyProfile'),
    path('myprofile/likes/',views.showLikes, name='MeLiked'),
    path('user/<username>/',
        views.showUserProfile, name='UserProfile'),
    path('user/<username>/likes/',
        views.showLikes, name='UserLiked'),

    path('<slug:continent_name_slug>/',
        views.home, name='show_continent'),
    path('<slug:continent_name_slug>/<slug:country_name_slug>/',
        views.home,name='Country'),
    path('<slug:continent_name_slug>/<slug:country_name_slug>/writereview/',
        views.writereview,name='write_review'),
    path('<slug:continent_name_slug>/<slug:country_name_slug>/<slug:city_name_slug>/',
        views.showreview,name='City'),
    path('<slug:continent_name_slug>/<slug:country_name_slug>/<slug:city_name_slug>/writereview/',
        views.writereview,name='City'),
]
