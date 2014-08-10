from django.db import models


class Database(models.Model):
    ENGINE_CHOICE_MYSQL = ('mysql', 'MySQL')
    ENGINE_CHOICE_POSTGRES = ('postgres', 'PostgreSQL')

    ENGINE_CHOICES = (
        ENGINE_CHOICE_MYSQL,
        ENGINE_CHOICE_POSTGRES,
    )

    name = models.CharField(max_length=60)
    db_name = models.CharField(max_length=255)
    db_host = models.CharField(max_length=255)
    db_user = models.CharField(max_length=255)
    db_password = models.CharField(max_length=255, blank=True)
    db_engine = models.CharField(max_length=255, choices=ENGINE_CHOICES)
    user = models.ForeignKey('auth.User', null=True, blank=True)
    organization = models.ForeignKey('organizations.Organization')

    def __unicode__(self):
        return self.name
