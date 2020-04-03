from django.test import TestCase
from django.contrib.auth.models import User
from GlobetrottersGuide.models import UserProfile,Continent,Country,City,countryReview,cityReview
from GlobetrottersGuide.forms import UserForm
from datetime import datetime

def makeCityReview(user,belong_city,title,rating,text,timeSpent,publishDate=datetime.now()):

    cityReview = cityReview.objects.get_or_create()[0]
    cityReview.username = user
    cityReview.belong_city = belong_city
    cityReview.rating = rating
    cityReview.text = text
    cityReview.time_spent = timeSpent
    cityReview.publishDate = publishDate

    cityReview.save()
    
    return cityReview

def makeCountryReview(user,belongCountry,rating,text,timeSpent,publishDate=datetime.now()):

    countryReview = countryReview.objects.get_or_create()[0]
    countryReview.username = user
    countryReview.belong_country = belongCountry
    countryReview.rating = rating
    countryReview.text = text
    countryReview.timeSpent = timeSpent
    countryReview.publishDate = publishDate

    countryReview.save()
    
    return countryReview

def makeUser(user,nationality,review_count,picture):
    user = UserProfile.objects.get_or_create(user=user)[0]
    user.picture = picture
    user.nationality = nationality
    user.review_count = review_count

    user.save()

    return user

def makeContinent(name,likes):
    continent = Continent.objects.get_or_create(name=name)[0]
    continent.likes = likes
    continent.Continent_id = 1
    continent.save()
    
    return continent

def makeCountry(name,continent,likes,views,review_count):
    country = Country.objects.get_or_create(name=name)[0]
    country.likes = likes
    country.views = views
    country.review_count = review_count
    country.continent = continent
    
    country.save()
    
    return country

def makeCity(name,country,likes,views,review_count):
    city = City.objects.get_or_create(name=name)[0]
    city.likes = likes
    city.views = views
    city.review_count = review_count
    city.Continent = continent
    
    city.save()
    
    return country

class testingUserDBModel(TestCase):
     
    ### checking if the fields exist
    ### most tests dont get to as Continent_id is missing (even though it doesnt exist)
        
    def testUsernameFieldExists(self):
        newobjUser = User.objects.create(username = 'useruser',password = 'password',first_name = 'David',last_name ='Hasselhoff',email='example@test.com')
        
        newContinent = makeContinent('Europe',32)
        newCountry = makeCountry('Denmark',newContinent,69,1337,57)
        
        newUser = makeUser(newobjUser,newCountry,12,'https://thumbs.dreamstime.com/b/smiling-old-man-having-coffee-portrait-looking-happy-33471677.jpg')
        
        userfield = newUser._meta.get_field('user').verbose_name
        self.assertEquals(userfield,'user')

    def testPictureFieldExists(self):
        newobjUser = User.objects.create(username = 'useruser',password = 'password',first_name = 'David',last_name ='Hasselhoff',email='example@test.com')
        
        newContinent = makeContinent('Europe',32)
        newCountry = makeCountry('Denmark',newContinent,69,1337,57)
        
        newUser = makeUser(newobjUser,newCountry,12,'https://thumbs.dreamstime.com/b/smiling-old-man-having-coffee-portrait-looking-happy-33471677.jpg')
        
        userfield = newUser._meta.get_field('picture').verbose_name
        self.assertEquals(userfield,'picture')
        
    def testNationalityFieldExists(self):
        newobjUser = User.objects.create(username = 'useruser',password = 'password',first_name = 'David',last_name ='Hasselhoff',email='example@test.com')
        
        newContinent = makeContinent('Europe',32)
        newCountry = makeCountry('Denmark',newContinent,69,1337,57)
        
        newUser = makeUser(newobjUser,newCountry,12,'https://thumbs.dreamstime.com/b/smiling-old-man-having-coffee-portrait-looking-happy-33471677.jpg')
        
        userfield = newUser._meta.get_field('nationality').verbose_name
        self.assertEquals(userfield,'nationality')
        
    def testReviewCountFieldExists(self):
        newobjUser = User.objects.create(username = 'useruser',password = 'password',first_name = 'David',last_name ='Hasselhoff',email='example@test.com')
        
        newContinent = makeContinent('Europe',32)
        newCountry = makeCountry('Denmark',newContinent,69,1337,57)
        
        newUser = makeUser(newobjUser,newCountry,12,'https://thumbs.dreamstime.com/b/smiling-old-man-having-coffee-portrait-looking-happy-33471677.jpg')
        
        userfield = newUser._meta.get_field('review_count').verbose_name
        self.assertEquals(userfield,'review count')
        
    def testLikedReviewCountryFieldExists(self):
        newobjUser = User.objects.create(username = 'useruser',password = 'password',first_name = 'David',last_name ='Hasselhoff',email='example@test.com')
        
        newContinent = makeContinent('Europe',32)
        newCountry = makeCountry('Denmark',newContinent,69,1337,57)
        
        newUser = makeUser(newobjUser,newCountry,12,'https://thumbs.dreamstime.com/b/smiling-old-man-having-coffee-portrait-looking-happy-33471677.jpg')
        
        userfield = newUser._meta.get_field('liked_review_country').verbose_name
        self.assertEquals(userfield,'liked review country')
        
    def testLikedReviewCityFieldExists(self):
        newobjUser = User.objects.create(username = 'useruser',password = 'password',first_name = 'David',last_name ='Hasselhoff',email='example@test.com')
        
        newContinent = makeContinent('Europe',32)
        newCountry = makeCountry('Denmark',newContinent,69,1337,57)
        
        newUser = makeUser(newobjUser,newCountry,12,'https://thumbs.dreamstime.com/b/smiling-old-man-having-coffee-portrait-looking-happy-33471677.jpg')
        
        userfield = newUser._meta.get_field('liked_review_city').verbose_name
        self.assertEquals(userfield,'liked review city')

    ###checking if fields are created properly
    def testFieldsExist(self):
        fields = list(User._meta.get_fields())
        self.assertNotEquals(fields,None)


class testingContinentDBModel(TestCase):
    ###checking if fields are created properly
    def testFieldsExist(self):
        newContinent = makeContinent('Europe',32)
        fields = list(newContinent._meta.get_fields())
        self.assertNotEquals(fields,None)
    
    ### checking if fields exist through the data
    def testNameExists(self):
        newContinent = makeContinent('Europe',32)
        field = newContinent._meta.get_field('name').verbose_name
    
        self.assertEquals(field,'name')
        
    def testLikesExists(self):
        newContinent = makeContinent('Europe',32)
        field = newContinent._meta.get_field('likes').verbose_name
        
        self.assertEquals(field,'likes')
        
    ###checking field specifics  
    def testNameLength(self):
        newContinent = makeContinent('Europe',32)
        field = Continent._meta.get_field('name').max_length
        
        self.assertEquals(field,128)

class testingCountryDBModel(TestCase):
    
    ###checking if fields exist from data creation
    ### most tests dont get to assert, due to Continent_id (which doesnt exist)
    
    def testNameExists(self):
        newContinent = makeContinent('Europe',32)
        newCountry = makeCountry('Denmark',newContinent,69,1337,57)
        field = newcountry._meta.get_field('name').verbose_name
        
        self.assertEquals(field,'name')
        
    def testViewsExists(self):
        newContinent = makeContinent('Europe',32)
        newCountry = makeCountry('Denmark',newContinent,69,1337,57)
        field = Country._meta.get_field('views').verbose_name
        
        self.assertEquals(field,'views')
    def testLikesExists(self):
        newContinent = makeContinent('Europe',32)
        newCountry = makeCountry('Denmark',newContinent,69,1337,57)
        field = Country._meta.get_field('likes').verbose_name
        
        self.assertEquals(field,'likes')
    def testReviewCountExists(self):
        newContinent = makeContinent('Europe',32)
        newCountry = makeCountry('Denmark',newContinent,69,1337,57)
        field = Country._meta.get_field('review_count').verbose_name
        
        self.assertEquals(field,'review count')
    
    def testContinentExists(self):
        newContinent = makeContinent('Europe',32)
        newCountry = makeCountry('Denmark',newContinent,69,1337,57)
        field = Country._meta.get_field('Continent').verbose_name
        
        self.assertEquals(field,'Continent')

    ### checking field attributes
    def testNameLength(self):
        field = Country._meta.get_field('name').max_length
        self.assertEquals(field,128)
    def testFieldsExist(self):
        newContinent = makeContinent('Europe',32)
        newCountry = makeCountry('Denmark',newContinent,69,1337,57)
        fields = list(newCountry._meta.get_fields())
        self.assertNotEquals(fields,None)
        


class testingCityDBModel(TestCase):
    ###checking if fields exist from data creation
    ### most tests dont get to assert, due to Continent_id (which doesnt exist)

    def testNameExists(self):
        newContinent = makeContinent('Europe',32)
        newCountry = makeCountry('Denmark',newContinent,69,1337,57)
        newCity = makeCity('Copenhagen',newCountry,50,50,25)
        
        field = newCity._meta.get_field('name').verbose_name
        self.assertEquals(field,'name')
    def testViewsExists(self):
        newContinent = makeContinent('Europe',32)
        newCountry = makeCountry('Denmark',newContinent,69,1337,57)
        newCity = makeCity('Copenhagen',newCountry,50,50,25)
        
        field = newCity._meta.get_field('views').verbose_name
        self.assertEquals(field,'views')
    def testLikesExists(self):
        newContinent = makeContinent('Europe',32)
        newCountry = makeCountry('Denmark',newContinent,69,1337,57)
        newCity = makeCity('Copenhagen',newCountry,50,50,25)
        
        field = newCity._meta.get_field('likes').verbose_name
        self.assertEquals(field,'likes')
    def testReviewCountExists(self):
        newContinent = makeContinent('Europe',32)
        newCountry = makeCountry('Denmark',newContinent,69,1337,57)
        newCity = makeCity('Copenhagen',newCountry,50,50,25)
        
        field = newCity._meta.get_field('review_count').verbose_name
        self.assertEquals(field,'review count')

    ### checking field attributes
    def testNameLength(self):
        field = City._meta.get_field('name').max_length
        self.assertEquals(field,128)
    def testFieldsExist(self):
        newContinent = makeContinent('Europe',32)
        newCountry = makeCountry('Denmark',newContinent,69,1337,57)
        newCity = makeCity('Copenhagen',newCountry,50,50,25)
        
        fields = list(newCity._meta.get_fields())
        self.assertNotEquals(fields,None)
    
        
        
        


    


    

    
    
    
        
