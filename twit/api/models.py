from django.db import models

# Create your models here.
"""
User Model
"""
class User(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    user_name = models.CharField()
    show_name = models.CharField()
    password = models.CharField()
    email = models.CharField()
    """
    TODO:
    List of Followers and Following
    Posts
    Messaging
    Encrypt Password
    """
