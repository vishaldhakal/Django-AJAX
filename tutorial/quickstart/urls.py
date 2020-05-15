from django.contrib import admin
from django.urls import path
from  .import views

urlpatterns = [
    path('', views.index,name='index'),
    path('plot/', views.plot,name='plot'),
    path('crud_ajax/', views.crud_ajax_create,name='crud_ajax_create'),
]