from django.db import models

class MywatchlistItem(models.Model):
    watched = models.CharField(max_length=5)
    title = models.CharField(max_length=50)
    rating = models.CharField(max_length=5)
    release_date = models.CharField(max_length=30)
    review = models.TextField()