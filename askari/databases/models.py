from django.db import models

class Database(models.Model):
    ENGINE_CHOICE_MYSQL = ('mysql', 'MySQL')
    ENGINE_CHOICE_POSTGRES = ('postgres', 'PostgreSQL')

    ENGINE_CHOICES = (
        ENGINE_CHOICE_MYSQL,
        ENGINE_CHOICE_POSTGRES,
    )

    name = models.CharField(max_length=60)
    host = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    engine = models.CharField(max_length=255, choices=ENGINE_CHOICES)

