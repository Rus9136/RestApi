from django.shortcuts import render
from rest_framework import generics
from .models import news
from .serializers import NewsSerializer


class NewsApiView(generics.ListAPIView):
    queryset = news.objects.all()
    serializer_class = NewsSerializer
