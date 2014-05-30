from django.db import models, connections


class Clip(models.Model):
    name = models.CharField(max_length=255)
    sql_query = models.TextField()
    database = models.ForeignKey('databases.Database')

    def __unicode__(self):
        return self.name

    def exec_query(self):
        alias = 'databases_{}'.format(self.pk)

        connections.databases[alias] = {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': self.database.db_name,
            'USER': self.database.user,
            'PASSWORD': self.database.password,
            'HOST': self.database.host,
            'PORT': '',
        }

        conn = connections[alias]

        cursor = conn.cursor()
        cursor.execute(self.sql_query)

        result_description = cursor.description
        result = cursor.fetchall()

        cursor.close()

        return (result, result_description)

