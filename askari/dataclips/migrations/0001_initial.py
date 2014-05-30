# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Clip'
        db.create_table(u'dataclips_clip', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('sql_query', self.gf('django.db.models.fields.TextField')()),
            ('database', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['databases.Database'])),
        ))
        db.send_create_signal(u'dataclips', ['Clip'])


    def backwards(self, orm):
        # Deleting model 'Clip'
        db.delete_table(u'dataclips_clip')


    models = {
        u'databases.database': {
            'Meta': {'object_name': 'Database'},
            'engine': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'host': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'dataclips.clip': {
            'Meta': {'object_name': 'Clip'},
            'database': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['databases.Database']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sql_query': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['dataclips']