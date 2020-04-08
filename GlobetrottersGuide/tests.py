from django.test import TestCase
from django.contrib.auth.models import User
from GlobetrottersGuide.models import UserProfile,Continent,Country,City,countryReview,cityReview
from GlobetrottersGuide.forms import UserForm
from django.db import IntegrityError
from datetime import datetime
import random
import string

def makeCountryReview(user,rating=0,text="",timeSpent=0,publishDate=datetime.now(),belongCountry,):

    CountryReview = countryReview.objects.get_or_create()[0]
    CountryReview.username = user
    CountryReview.belong_country = belongCountry
    CountryReview.rating = rating
    CountryReview.text = text
    CountryReview.timeSpent = timeSpent
    CountryReview.publishDate = publishDate

    CountryReview.save()
    
    return CountryReview

def makeCityReview(user,title,rating,text,timeSpent,publishDate=datetime.now()):

    CityReview = cityReview.objects.get_or_create()[0]
    CityReview.username = user
    CityReview.belong_city = belong_city
    CityReview.rating = rating
    CityReview.text = text
    CityReview.time_spent = timeSpent
    CityReview.publishDate = publishDate

    CityReview.save()
    
    return CityReview

def makeUser(user,review_count,picture,nationality):
    user = UserProfile.objects.get_or_create(user=user)[0]
    user.picture = picture
    user.nationality = nationality
    user.review_count = review_count

    user.save()

    return user

def makeContinent(name,likes=0):
    continent = Continent.objects.get_or_create(name=name)[0]
    continent.likes = likes
    continent.save()
    
    return continent

def makeCountry(name,continent=1,likes=0,views=0,review_count=0,continent_id = 1):
    country = Country.objects.get_or_create(name=name)[0]
    country.likes = likes
    country.views = views
    country.review_count = review_count
    country.continent = continent
    country.Continent_id = continent_id
    
    country.save()
    
    return country

def makeCity(name,country=1,likes=0,views=0,review_count=0):
    city = City.objects.get_or_create(name=name)[0]
    city.likes = likes
    city.views = views
    city.review_count = review_count
    city.country = country
    
    city.save()
    
    return country


def makeLongString():
    rnd = ''.join([random.choice(string.ascii_letters)for i in range(129)])
    return rnd
    

class testingContinentModel(TestCase):

    def testContinentName(self):
        newContinent = makeContinent('Europe')
        NC = Continent.objects.get(name='Europe')
        field = NC._meta.get_field('name').verbose_name
        self.assertEquals(field,'name')
        
    def fieldsExist(self):
        
        aContinent = Continent.objects.get_fields()
        self.assertNotEquals(list(aContinent),None)
        
    def ifContinentHasLongerName(self):
        newContinent = makeContinent(makeLongString())
        self.assertRaises(Exception,newContinent)
        
    def testSlug(self):
        newContinent = makeContinent('this is a random string')
        newcontinent.save()

        self.assertEqual(newContinent.slug,'this-is-a-random-string')
        
    def likesAreNotNegative(self):
        newContinent = makeContinent('Europe',-3124)
        self.assertEqual((newContinent.likes >= 0),True)
    
        
class testingCountryModel(TestCase):
    
    def fieldsExist(self):
        aCountry = Country.objects.get_fields()
        self.assertNotEquals(list(aCountry),None)
        
    def ifCountryHasLongerName(self):
        newCountry = makeCountry(makeLongString())
        self.assertRaises(Exception,newCountry)
        
    def testSlug(self):
        newCountry = makeCountry('oh look another string')
        newCountry.save()

        self.assertEqual(newCountry,'oh-look-another-random-string')
        
    def viewsNotNegative(self):
        newCountry = makeCountry('Belgium',views = -548)
        self.assertEqual((newCountry.views >= 0), True)
        
    def likesNotNegative(self):
        newCountry = makeCountry('Belgium',likes = -10)
        self.assertEqual((newCountry.likes >= 0), True)
        
    def continentIsNotNone(self):
        newCountry = makeCountry('Belgium',continent = None)
        self.assertRaises(IntegrityError,newCountry)
        
    def reviewCountNotNegative(self):
        newCountry = makeCountry('Belgium',review_count = -35135)
        self.assertEqual((newCountry.review_count >= 0),True)
        
class testingCityModel(TestCase):

    def fieldsExist(self):
        aCity = City.objects.get_fields()
        self.assertNotEquals(list(aCity),None)
        
    def ifCountryHasLongerName(self):
        newCountry = makeCity(makeLongString())
        self.assertRaises(Exception,newCountry)
        
    def testSlug(self):
        newCountry = makeCity('AND ANOTHER ONE')
        newCountry.save()

        self.assertEqual(newCountry,'AND-ANOTHER-ONE')
        
    def viewsNotNegative(self):
        newCity = makeCountry('Brussels',views = -233)
        self.assertEqual((newCity.views >= 0), True)
        
    def likesNotNegative(self):
        newCity = makeCity('Brussels',likes = -3)
        self.assertEqual((newCity.likes >= 0), True)
        
    def countryIsNotNone(self):
        newCity = makeCity('Brussels',country = None)
        self.assertRaises(IntegrityError,newCity)
        
    def reviewCountNotNegative(self):
        newCity = makeCity('Brussels',review_count = -35135)
        self.assertEqual((newCity.review_count >= 0),True)
    

class testingUserModel(TestCase):
        
    def positiveReviewCount(self):
        userinstance = makeUser('StewartC',review_count = -1)
        self.assertEqual((userinstance.review_count>=0),True)
        
    def slugTest(self):
        userinstance = makeUser('travelling tourist 73')
        self.assertEqual(userinstance.slug,'travelling-tourist-73')
                
