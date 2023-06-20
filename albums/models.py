from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.


class Album(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    artist = models.ForeignKey(
        to='Artist', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    cover = models.ImageField(upload_to='images', blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
