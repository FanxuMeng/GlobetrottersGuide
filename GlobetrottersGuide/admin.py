from django.contrib import admin
from GlobetrottersGuide.models import Continent, Country, City
from GlobetrottersGuide.models import countryReview, cityReview
from GlobetrottersGuide.models import UserProfile

class ContinentAdmin(admin.ModelAdmin):
    list_display = ('name', 'likes')
    prepopulated_fields = {'slug': ('name',)}

class CountryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class countryReviewAdmin(admin.ModelAdmin):
    model = countryReview
    list_display = ('user', 'publish_date', 'belong_country')

class cityReviewAdmin(admin.ModelAdmin):
    model = cityReview
    list_display = ('user', 'publish_date', 'belong_city')

admin.site.register(Continent, ContinentAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(UserProfile)
admin.site.register(countryReview, countryReviewAdmin)
admin.site.register(cityReview, cityReviewAdmin)