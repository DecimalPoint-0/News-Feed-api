from rest_framework import serializers
from Newsfeed import models

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for the user profile creation,updating and deleting"""
    class Meta:
        model = models.UserProfile
        fields = ['id','email', 'name', 'password', 'contact', 'api_key']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            },
            'contact': {
                'style': {'input_type': 'number'}
            }
        }

    def create(self, validated_data):
        """Validate user credential and return User"""
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password'],
            contact = validated_data['contact']
        )

        return user