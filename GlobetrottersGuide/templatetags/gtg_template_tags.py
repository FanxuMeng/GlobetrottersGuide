from django import template

from GlobetrottersGuide.models import Continent
from GlobetrottersGuide.models import Country
from GlobetrottersGuide.models import City

register = template.Library()

@register.inclusion_tag('GlobetrottersGuide/home.html')
def get_continet_list(current_continet=None):
    return {'continent':Continent.objects.all(),
            'current_continet':current_continet}

@register.inclusion_tag('GlobetrottersGuide/home_country.html')
def get_city_list(current_city=None):
    return {'city':City.objects.all(),
            'current_city':current_city}

@register.inclusion_tag('GlobetrottersGuide/home_continent.html')
def get_country_list(current_country=None):
    return {'country':Country.objects.all(),
            'current_country':current_country}

