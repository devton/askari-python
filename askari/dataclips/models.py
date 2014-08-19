from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

import json

from django.core.cache import cache
from django.db import models, connections
from django.db.models.signals import pre_save

from .managers import ClipScopeManager
from .signals import ClipSignal
from ..core.tags.models import Tagged

@python_2_unicode_compatible
class Clip(Tagged):
    name = models.CharField(max_length=255)
    sql_query = models.TextField()
    slug = models.SlugField()
    user = models.ForeignKey('auth.User',
                             null=True,
                             blank=True,
                             on_delete=models.DO_NOTHING)
    database = models.ForeignKey('databases.Database', 
                                 on_delete=models.CASCADE)
    organization = models.ForeignKey('organizations.Organization',
                                     on_delete=models.CASCADE)

    objects = ClipScopeManager()

    original_sql_query = None

    def __unicode__(self):
        return self.name

    def cache_key(self):
        return "dataclips_{}".format(self.pk)

    # Override class constructor to get the initial sql_query 
    # to turn possible to make a comparsion when clip is saved
    def __init__(self, *args, **kwargs):
        super(Clip, self).__init__(*args, **kwargs)
        self.original_sql_query = self.sql_query

    # Override save to set the new sql_query when changed
    # to turn possible to make a comparsion when clip is saved
    def save(self, *args, **kwargs):
        super(Clip, self).save(*args, **kwargs)
        self.original_sql_query = self.sql_query

    def query_result(self):
        """
          Return a cached clip.sql_query executed
          suck like a:
          {'rows': [['foo', 'bar'], ['foo']], 'cols': ['col1', 'col2']}
        """

        cached = cache.get(self.cache_key())
        if cached is not None:
            return json.loads(cached)
        else:
            try:
                self.dump_query()
                return self.query_result()
            except Exception:
                return self.__exec_query()

    def dump_query(self):
        """
          Execute the sql query and make a cache
          accessible using:
          cache.get(self.cache_key())
        """

        cache.delete(self.cache_key())

        r = self.__exec_query()
        dump = json.dumps({'rows': r['rows'], 'cols': r['cols']})

        return cache.set(self.cache_key(), dump, 50000)

    def __exec_query(self):
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
        sql = "select _.* from ({}) as _ limit 10000".format(self.sql_query)
        cursor.execute(sql)

        result_description = cursor.description
        result = cursor.fetchall()

        cursor.close()

        del connections.databases[alias]
        del connections[alias]

        self._sql_result = (result, result_description)
        return self.__format_query_result()

    def __format_query_result(self):
        result = self._sql_result

        # Create a array with all query result values
        row_details = []
        for item in result[0]:
            values = []
            for value in item:
                values.append(value)
            row_details.append(values)

        # Create a awway with all query result columns
        col_details = []
        for item in result[1]:
            col_details.append(item.name)

        return {'rows': row_details, 'cols': col_details}


pre_save.connect(ClipSignal.pre_save, sender=Clip)
