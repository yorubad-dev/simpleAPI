from django.shortcuts import render
from .models import Article
from .serializer import ArticleSerializer
from rest_framework import generics
from rest_framework import mixins

# Create your views here.
class GenericApiView(generics.GenericAPIView, mixins.ListModelMixin):
    def get(self, request):
        return self.list(request)
