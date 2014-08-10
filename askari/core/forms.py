# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from .user_profile.models import UserProfile
from ..organizations.models import Organization


User = get_user_model()


class UserRegistrationForm(UserCreationForm):
    organization_name = forms.CharField(required=True, label="Organização")
    organization_slug = forms.SlugField(required=True,
                                        label="Namespace (/namespace)")

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_organization_slug(self):
        try:
            Organization.objects.get(
                slug=self.cleaned_data['organization_slug'])
            raise forms.ValidationError("Essa organização já existe")
        except Organization.DoesNotExist:
            pass

    @transaction.atomic
    def save(self, *args, **kwargs):
        user = super(UserRegistrationForm, self).save(*args, **kwargs)

        profile = UserProfile.objects.create(user=user)
        organization = Organization.objects.create(
            name=self.cleaned_data['organization_name'],
            slug=self.cleaned_data['organization_slug'])

        profile.organizations.add(organization)

        return user
