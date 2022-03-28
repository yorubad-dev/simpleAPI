from django.shortcuts import render
from .models import Article
from .serializer import ArticleSerializer
from rest_framework import generics
from rest_framework import mixins

# Create your views here.


class GenericApiView(generics.GenericAPIView, mixins.ListModelMixin,
                     mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request):
        return self.update(request)

    def delete(self, request):
        return self.destroy(request)
