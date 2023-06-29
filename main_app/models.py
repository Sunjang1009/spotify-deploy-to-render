from django.db import models
import time 


# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    bio = models.CharField(max_length=500)
    verified_artist = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
# this is a way to save the order of the names. Alphabetically sorted
    def __str__(self):
        return "Artist: " + self.name

    class Meta:
        ordering = ['name']

class Song(models.Model):
    title = models.CharField(max_length=150)
    length = models.IntegerField(default=0)
    # primaey key will be Artist pk
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="songs")
    # def does not need migrate
    def __str__(self):
        return self.title

    def get_length(self):
        return time.strftime("%M:%S", time.gmtime(self.length))


class Playlist(models.Model):
    title = models.CharField(max_length=150)
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.title


