from django.shortcuts import render

from Newsfeed import models
from Newsfeed import serializers, permissions

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated


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


class NewsFeed(viewsets.ModelViewSet):
    """News Feed creation, deletion, and updating"""
    queryset = models.Post.objects.all()
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.NewsSerializer
    permission_classes = (IsAuthenticated, permissions.IsAdminOrReadOnly, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('title', 'content', 'created_at', )

    def perform_create(self, serializer):
        """Sets the author of the news to the logged in user"""
        serializer.save(author=self.request.user)