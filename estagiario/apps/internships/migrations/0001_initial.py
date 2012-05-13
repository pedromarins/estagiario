# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Internship'
        db.create_table('internships_internship', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=180)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('complement', self.gf('django.db.models.fields.CharField')(max_length=180, null=True, blank=True)),
            ('district', self.gf('django.db.models.fields.CharField')(max_length=180, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['address.City'])),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['address.State'])),
            ('cep', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('field', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['internships.Field'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, blank=True)),
            ('company_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('company_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('company_img', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True)),
            ('company_size', self.gf('django.db.models.fields.CharField')(default='peq', max_length=5)),
            ('weekly_hours', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('salary', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=2)),
            ('min_semester', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('transport', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('health', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('food', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('flexible_hours', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('relevance', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('featured', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('expiration', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('internships', ['Internship'])

        # Adding model 'Field'
        db.create_table('internships_field', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=(), max_length=50, populate_from=None)),
        ))
        db.send_create_signal('internships', ['Field'])


    def backwards(self, orm):
        # Deleting model 'Internship'
        db.delete_table('internships_internship')

        # Deleting model 'Field'
        db.delete_table('internships_field')


    models = {
        'address.city': {
            'Meta': {'object_name': 'City'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '180'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['address.State']"})
        },
        'address.state': {
            'Meta': {'object_name': 'State'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '180'}),
            'uf': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'internships.field': {
            'Meta': {'object_name': 'Field'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': 'None'})
        },
        'internships.internship': {
            'Meta': {'object_name': 'Internship'},
            'cep': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['address.City']"}),
            'company_img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'company_size': ('django.db.models.fields.CharField', [], {'default': "'peq'", 'max_length': '5'}),
            'company_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'complement': ('django.db.models.fields.CharField', [], {'max_length': '180', 'null': 'True', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '180', 'null': 'True', 'blank': 'True'}),
            'expiration': ('django.db.models.fields.DateField', [], {}),
            'featured': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'field': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['internships.Field']"}),
            'flexible_hours': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'food': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'health': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'min_semester': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'relevance': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'salary': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '2'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['address.State']"}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '180'}),
            'transport': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'weekly_hours': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        'taggit.taggeditem': {
            'Meta': {'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'taggit_taggeditem_tagged_items'", 'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'taggit_taggeditem_items'", 'to': "orm['taggit.Tag']"})
        }
    }

    complete_apps = ['internships']