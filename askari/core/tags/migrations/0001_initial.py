# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tag'
        db.create_table(u'tags_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200, db_index=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=150)),
        ))
        db.send_create_signal(u'tags', ['Tag'])

        # Adding unique constraint on 'Tag', fields ['slug', 'name']
        db.create_unique(u'tags_tag', ['slug', 'name'])


    def backwards(self, orm):
        # Removing unique constraint on 'Tag', fields ['slug', 'name']
        db.delete_unique(u'tags_tag', ['slug', 'name'])

        # Deleting model 'Tag'
        db.delete_table(u'tags_tag')


    models = {
        u'tags.tag': {
            'Meta': {'unique_together': "(['slug', 'name'],)", 'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200', 'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['tags']