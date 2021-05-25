from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [

    url(r'^gallery/index/$', views.index, name='galleryIndex'),
    url(r'^gallery/img/detail/(?P<pk>\d+)/$', views.image_details, name='galleryImgDetails'),

]