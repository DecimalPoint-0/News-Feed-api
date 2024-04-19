from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
import secrets

class UserProfileManager(BaseUserManager):
    """Baseuser for creating user profiles"""

    def create_user(self, email, name, contact, password=None):
        """creates a new user profile"""
        if not email:
            raise ValueError("User does not have an email address")
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, contact=contact)
        
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, name, password, contact='09012024759'):
        """Create a new super user"""
        user = self.create_user(email, name, contact, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user
    

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    contact = models.IntegerField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """retrieve and return full name"""
        return self.name
    
    def get_email(self):
        """retrieve email address of user"""
        return self.email
    
    def __str__(self):
        """return string representation of user"""
        return self.email


class Category(models.Model):
    """Creates categories of news"""
    category_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        """Returns the string representation of the obj (category)"""
        return self.category_name


class Post(models.Model):
    """Model for Posts / News """
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.FileField(upload_to='images')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title