from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from .models import Video
# Create your views here.

class VideoListSerializer(serializers.ModelSerializer):
    model = Video
    fields = '__all__'

class VideoDetailUpdateAPIView(viewsets.GenericViewSet, RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoListSerializer
    lookup_field = 'id'
    # permission_classes = [IsAuthenticated]

class VideoListCreateAPIView(viewsets.GenericViewSet, ListCreateAPIView):
    serializer_class = VideoListSerializer
    queryset = Video.objects.all()
    