from django.urls import path

from . import views

path('article/', views.GenericApiView.as_view())