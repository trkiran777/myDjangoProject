# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Provider.series_list'
        db.alter_column(u'contact_web_app_provider', 'series_list', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=70))

    def backwards(self, orm):

        # Changing field 'Provider.series_list'
        db.alter_column(u'contact_web_app_provider', 'series_list', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=50))

    models = {
        u'contact_web_app.contact': {
            'Meta': {'object_name': 'Contact'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'phone_no': ('django.db.models.fields.CharField', [], {'max_length': '10', 'primary_key': 'True'}),
            'pin_code': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        },
        u'contact_web_app.provider': {
            'Meta': {'object_name': 'Provider'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'provider_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'series_list': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '70'})
        }
    }

    complete_apps = ['contact_web_app']