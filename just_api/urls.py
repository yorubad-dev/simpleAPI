from django.urls import path

from . import views
urlpatterns = [
    path('article/', views.GenericApiView.as_view())
]
