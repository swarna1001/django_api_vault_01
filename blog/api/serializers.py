from django.db.models import fields
from rest_framework import serializers
from .models import BlogPost

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogPost
        fields = ('title', 'body', 'created_at')

