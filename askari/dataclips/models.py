import json

from django.core.cache import cache
from django.db import models, connections
from django.db.models.signals import pre_save

from .signals import ClipSignal
from ..core.tags.models import Tagged


class Clip(Tagged):
    name = models.CharField(max_length=255)
    sql_query = models.TextField()
    database = models.ForeignKey('databases.Database')
    slug = models.SlugField()

    def __unicode__(self):
        return self.name

    def cache_key(self):
        return u"dataclips_{}".format(self.pk)

    def query_result(self):
        cached = cache.get(self.cache_key())
        if cached is not None:
            return json.loads(cached)
        else:
            try:
                self.dump_query()
                return self.query_result()
            except:
                return self.exec_query()

    def dump_query(self):
        cache.delete(self.cache_key())

        r = self.exec_query()
        dump = json.dumps({'rows': r['rows'], 'cols': r['cols']})

        return cache.set(self.cache_key(), dump, 50000)

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
        sql = "select _.* from ({}) as _ limit 10000".format(self.sql_query)
        cursor.execute(sql)

        result_description = cursor.description
        result = cursor.fetchall()

        cursor.close()

        del connections.databases[alias]
        del connections[alias]

        self._query_result = (result, result_description)
        return self.format_query_result()

    def format_query_result(self):
        result = self._query_result

        # Create a array with all query result values
        row_details = []
        for item in result[0]:
            values = []
            for value in item:
                values.append(unicode(value))
            row_details.append(values)

        # Create a awway with all query result columns
        col_details = []
        for item in result[1]:
            col_details.append(unicode(item.name))

        return {'rows': row_details, 'cols': col_details}


pre_save.connect(ClipSignal.pre_save, sender=Clip)
