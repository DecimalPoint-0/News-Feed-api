from django.contrib import admin
from Newsfeed import models
# Register your models here.

admin.site.register(models.UserProfile)
admin.site.register(models.Post)
admin.site.register(models.Category)