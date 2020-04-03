#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from GlobetrottersGuide.models import UserProfile, editProfile
from GlobetrottersGuide.models import countryReview, cityReview
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Mate:
        model = User
        fields = ('username', 'password')


class UserProfileForm(forms.ModelForm):
    class Mata:
        model = UserProfile
        fields = ('picture', 'nationality')

class EditProfileForm(forms.ModelForm):
    username = forms.CharField(label='username')
    nationality = forms.CharField(label='nationality') 

    class Meta:
        model = UserProfile
        fields = ('username', 'nationality')


class countryReviewForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows':40,'cols':20}),
                           max_length=countryReview.TEXT_MAX_LENGTH,
                           help_text='Share your experience.')

    class Mate:
        model = countryReview
        fields = ('timeSpent', 'image', 'text', 'belong_country')


class cityReviewForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows':40,'cols':20}),
                           max_length=cityReview.TEXT_MAX_LENGTH,
                           help_text='Share your experience.')

    class Mate:
        model = cityReview
        fields = ('timeSpent', 'image', 'text', 'belong_city')
