#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from GlobetrottersGuide.models import UserProfile
from GlobetrottersGuide.models import Review
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Mate:
        model = User
        fields = ('username', 'password')

class UserProfileForm(forms.ModelForm):
    class Mata:
        model = UserProfile
        fields = ('picture', 'nationality')

class ReviewForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows':40,'cols':20}),
                           max_length=Review.TEXT_MAX_LENGTH,
                           help_text='Share your experience.')

    class Mate:
        model = Review
        fields = ('timeSpent', 'image', 'text', 'belong_country', 'belong_city')
