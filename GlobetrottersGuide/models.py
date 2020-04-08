from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Continent(models.Model):
    NAME_MAX_LENGTH = 128

    name = models.CharField(max_length=128, unique=True)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    reviewNum = 0

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Continent, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Country(models.Model):
    NAME_MAX_LENGTH = 128

    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    flag = models.ImageField(upload_to='flags',blank=True)
    slug = models.SlugField(unique=True)
    reviewNum = 0

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Country, self).save(*args, **kwargs)

    def getContinentSlug(self):
        return self.continent.slug
    
    def getContinent(self):
        return self.continent

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name


class City(models.Model):
    NAME_MAX_LENGTH = 128

    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    reviewNum = 0

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(City, self).save(*args, **kwargs)
    
    def getCountrySlug(self):
        return self.country.slug
    
    def getCountry(self):
        return self.country

    class Meta:
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name


class countryReview(models.Model):
    TEXT_MAX_LENGTH = 2000

    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    belong_country = models.ForeignKey(Country, on_delete=models.CASCADE)

    publish_date = models.DateTimeField('date published')
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    timeSpent = models.DurationField(blank=False)
    image = models.ImageField(upload_to='review_images', blank=True)
    title = models.CharField(max_length=128, default='Title')
    text = models.TextField(max_length=2000, blank=False)
    rating = models.IntegerField(choices=RATING_CHOICES)


class cityReview(models.Model):
    TEXT_MAX_LENGTH = 2000

    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    belong_city = models.ForeignKey(City, on_delete=models.CASCADE)

    publish_date = models.DateTimeField('date published')
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    timeSpent = models.DurationField(blank=False)
    image = models.ImageField(upload_to='review_images', blank=True)
    title = models.CharField(max_length=128, default='Title')
    text = models.TextField(max_length=2000, blank=False)
    rating = models.IntegerField(choices=RATING_CHOICES)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    nationality = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.user.username
