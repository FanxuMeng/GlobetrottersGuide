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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.urls import include
from GlobetrottersGuide import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('GlobetrottersGuide.urls')),
    path('accounts/',include('registration.backends.simple.urls')),

    path('user/<int:user_id>/',
        views.showUserProfile, name='UserProfile'),
    path('user/<int:user_id>/likes/',
        views.showLikes, name='UserLiked'),


    path('<slug:continent_name_slug>/',
        views.home_continent, name='Continent'),
    path('<slug:continent_name_slug>/<slug:country_name_slug>/',
        views.home_country,name='Country'),
    path('<slug:continent_name_slug>/<slug:country_name_slug>/<slug:city_name_slug>/',
        views.home_city,name='City'),
    path('writeCountryReview/',
        views.add_countryReview,name='Reviewing'),
    path('writeCityReview/',
        views.add_cityReview,name='Reviewing'),
    path('<slug:continent_name_slug>/<slug:country_name_slug>/<int:cityReview_id>/',
         views.review_detail, name='review'),
    path('<slug:continent_name_slug>/<int:countryReview_id>/',
         views.review_detail, name='review'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
