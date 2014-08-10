from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField('auth.User')
    organizations = models.ManyToManyField('organizations.Organization', 
                                           null=True, 
                                           blank=True)

