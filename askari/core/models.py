from django.db import models
from django.contrib.auth.models import User
from ..databases.models import Database
from ..dataclips.models import Clip


class ProxyUser(User):

    def databases(self):
        '''
            Return the user databases
        '''
        return Database.objects.filter(user__pk=self.pk).all()

    def clips(self):
        '''
            Return the user dataclips
        '''
        return Clip.objects.filter(database__user__pk=self.pk).all()


    class Meta():
        proxy = True