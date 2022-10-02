from django.db import models

class WishlistFilmKu(models.Model):
    film_watched = models.BooleanField()
    film_title = models.TextField()
    film_rating = models.IntegerField()
    film_release_date = models.TextField()
    film_review = models.TextField()
