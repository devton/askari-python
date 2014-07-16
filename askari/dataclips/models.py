from django.db import models, connections
from django.db.models.signals import pre_save
from .signals import ClipSignal


class Clip(models.Model):
    name = models.CharField(max_length=255)
    sql_query = models.TextField()
    database = models.ForeignKey('databases.Database')
    slug = models.SlugField()

    def __unicode__(self):
        return self.name

    def exec_query(self):
        alias = 'databases_{}'.format(self.pk)

        connections.databases[alias] = {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': self.database.db_name,
            'USER': self.database.db_user,
            'PASSWORD': self.database.db_password,
            'HOST': self.database.db_host,
            'PORT': '',
        }

        conn = connections[alias]

        cursor = conn.cursor()
        sql = "select * from ({}) limit 10000".format(self.sql_query)
        cursor.execute(sql)

        result_description = cursor.description
        result = cursor.fetchall()

        cursor.close()

        del connections.databases[alias]
        del connections[alias]

        return (result, result_description)


pre_save.connect(ClipSignal.pre_save, sender=Clip)
