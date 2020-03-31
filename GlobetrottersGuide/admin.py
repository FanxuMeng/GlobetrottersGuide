from django.contrib import admin
from GlobetrottersGuide.models import Continent, Country, City
from GlobetrottersGuide.models import Review
from GlobetrottersGuide.models import UserProfile

class ContinentAdmin(admin.ModelAdmin):
    list_display = ('name', 'likes')
    prepopulated_fields = {'slug': ('name',)}

class CountryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('user', 'publish_date', 'belong_country', 'belong_city')

admin.site.register(Continent, ContinentAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(UserProfile)
admin.site.register(Review, ReviewAdmin)
