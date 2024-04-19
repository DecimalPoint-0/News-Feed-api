from django.urls import path, include

from Newsfeed import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('profile', views.UserProfile, basename='user_viewset')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.UserLoginView.as_view(), name='login_view'),
    path('key/', views.GenerateAPI.as_view(), name='api_key'),
]