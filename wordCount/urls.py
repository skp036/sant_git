
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [

    path('', views.homepage, name='index'),
    path('word-counter.html', views.count_method, name='count'),
    path('webmaster/', admin.site.urls, name='admin')
]
