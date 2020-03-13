from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Continent(models.Model):
    NAME_MAX_LENGTH = 128

    name = models.CharField(max_length=128, unique=True)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Continent, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Country(models.Model):
    NAME_MAX_LENGTH = 128

    Continent = models.ForeignKey(Continent, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    review_count = models.IntegerField(default=0)
    flag = models.ImageField(upload_to='flags',blank=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Country, self).save(*args, **kwargs)

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
    review_count = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(City, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name


class Review(models.Model):
    TEXT_MAX_LENGTH = 2000

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    timeSpent = models.DurationField(blank=False)
    image = models.ImageField(upload_to='review_images', blank=True)
    text = models.TextField(max_length=2000, blank=False)

    belong_country = models.OneToOneField(Country, on_delete=models.CASCADE, blank=True)
    belong_city = models.OneToOneField(City, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.user


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    nationality = models.ForeignKey(Country, on_delete=models.CASCADE)
    review_count = models.IntegerField(default=0)

    liked_review = models.ManyToManyField(Review,on_delete=models.CASCADE)
    liked_country = models.ManyToManyField(Country,on_delete=models.CASCADE)
    liked_city = models.ManyToManyField(City,on_delete=models.CASCADE)

    def __str__(self):
        return self.user
