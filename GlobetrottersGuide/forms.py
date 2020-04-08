#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from GlobetrottersGuide.models import UserProfile
from GlobetrottersGuide.models import countryReview, cityReview
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
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
    timeSpent = forms.DurationField()
    title = forms.CharField(widget=forms.Textarea(attrs={'rows': 1, 'cols': 20}))
    image = forms.ImageField()
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 40, 'cols': 20}),
                           max_length=countryReview.TEXT_MAX_LENGTH,
                           help_text='Share your experience.')

    class Mate:
        model = countryReview
        fields = ('title', 'timeSpent', 'image', 'text')

    def clean(self):
        cleaned_data = self.cleaned_data
        timeSpent = cleaned_data.get('timeSpent')
        timeSpent = f'{timeSpent} days'
        cleaned_data['timeSpent'] = timeSpent

        return cleaned_data


class cityReviewForm(forms.ModelForm):
    timeSpent = forms.DurationField()
    title = forms.CharField(widget=forms.Textarea(attrs={'rows': 1, 'cols': 20}))
    image = forms.ImageField()
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 40, 'cols': 20}),
                           max_length=countryReview.TEXT_MAX_LENGTH,
                           help_text='Share your experience.')

    class Mate:
        model = cityReview
        fields = ('title', 'timeSpent', 'image', 'text')

    def clean(self):
        cleaned_data = self.cleaned_data
        timeSpent = cleaned_data.get('timeSpent')
        timeSpent = f'{timeSpent} days'
        cleaned_data['timeSpent'] = timeSpent

        return cleaned_data
