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
    followers = models.ManyToManyField(User, relate_name="followers")
    following = models.ManyToManyField(User, related_name="following")
    """
    TODO:
    Messaging
    Encrypt Password
    """

class Post(models.Model):
    message = models.CharField()
    author = models.ForeignKeyField(User, on_delete=models.CASCADE)
    likes = models.IntegerField()
    retwits = models.IntegerField()
