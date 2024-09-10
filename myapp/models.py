from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='movies/')
    likes = models.ManyToManyField(User, related_name='liked_movies', blank=True)

    def __str__(self):
        return self.title
