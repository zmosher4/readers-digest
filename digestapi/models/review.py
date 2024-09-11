from django.db import models
from django.contrib.auth.models import User
from .book import Book


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    number_rating = models.IntegerField()
    comment = models.CharField(max_length=200)
    date_posted = models.DateTimeField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
