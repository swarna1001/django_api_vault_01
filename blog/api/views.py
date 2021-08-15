from django.shortcuts import render
from django.http.response import JsonResponse
from .models import BlogPost
from .serializers import BlogSerializer
from rest_framework import generics


class BlogList(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogSerializer

    
