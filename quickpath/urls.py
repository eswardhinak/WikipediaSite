from django.conf.urls import patterns, url
from quickpath import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        #add new urls here
        )