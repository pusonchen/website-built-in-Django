# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
 
class News(models.Model):
    headline = models.CharField(max_length=70)
    news_class = models.CharField(max_length=70)
    pub_time = 	models.DateTimeField()
    news_text = models.TextField(max_length=200)
    def __unicode__(self):  
        return self.headline

class NewsAdmin(admin.ModelAdmin):
    list_display=('headline','pub_time','news_text')
    list_filter=('pub_time',)
    date_hierarchy='pub_time'
    ordering=('-pub_time',)        
     
class Bussiness_Support(models.Model):   
    name = models.CharField(max_length=20)
    place = models.CharField(max_length=20)
    text = models.TextField(max_length=200)
    def __unicode__(self):  
        return self.name

        
class Member(models.Model):
    name = models.CharField(max_length=70)
    title = models.CharField(max_length=70)
    email = models.EmailField(blank=True)
    description = models.TextField(max_length=200)
    def __unicode__(self):  
        return self.name

		