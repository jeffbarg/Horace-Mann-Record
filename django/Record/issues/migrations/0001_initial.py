# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Issue'
        db.create_table(u'issues_issue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('volume', self.gf('django.db.models.fields.IntegerField')()),
            ('issue', self.gf('django.db.models.fields.IntegerField')()),
            ('printissue', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')()),
            ('date_published', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'issues', ['Issue'])


    def backwards(self, orm):
        # Deleting model 'Issue'
        db.delete_table(u'issues_issue')


    models = {
        u'issues.issue': {
            'Meta': {'object_name': 'Issue'},
            'date_published': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.IntegerField', [], {}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {}),
            'printissue': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'volume': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['issues']