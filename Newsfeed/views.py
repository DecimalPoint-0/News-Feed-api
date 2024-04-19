from django.shortcuts import render

from Newsfeed import models

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings
import secrets

from Newsfeed import serializers, permissions


class UserProfile(viewsets.ModelViewSet):
    """Creates and Updates User Profile"""
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile, IsAuthenticated,)
    serializer_class = serializers.UserProfileSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(id=self.request.user.id)  


class UserLoginView(ObtainAuthToken):
    """Log user in and assigns an authentication token to them"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class GenerateAPI(APIView):
    """Generates and Displays API Key"""
    def get(self, request):
        user = models.UserProfile.objects.get(id=request.user.id)
        if user.api_key == "None":
            api_key = secrets.token_hex(16)
            user.api_key = api_key
            user.save()
        return Response({'API_KEY': api_key})


class NewsFeed(viewsets.ModelViewSet):
    """News Feed"""
    queryset = models.Post.objects.all()
