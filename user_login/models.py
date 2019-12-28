from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class ProfileUser(models.Model):

    user = models.OneToOneField(User, on_delete = models.CASCADE)
    profilepics = models.ImageField(upload_to='profilepics', default='default.jpg')

    def __str__(self):

        return self.user.username

class Post(Model):

    title = models.CharField(max_length=200)
    last_modified = models.DateTimeField(default = timezone.now())
    created_by = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    types_of_blog = (
        ('en', 'entertainment'),
        ('ls', 'lifestyle'),
        ('edu', 'education'),
        ('play', 'sports')
    )
    type_blog = models.CharField(max_length=10, choices= types_of_blog)
    blog_des =  models.TextField(blank=True)

    def __str__(self):

        return self.title
