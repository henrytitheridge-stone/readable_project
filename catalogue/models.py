from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

RATING = ((1, "1/5 stars"),
          (2, "2/5 stars"),
          (3, "3/5 stars"),
          (4, "4/5 stars"),
          (5, "5/5 stars"))


# Create your models here.
class Book(models.Model):
    """
    Stores a single book in the catalogue, related to :model: `auth:User`
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.CharField(max_length=200)
    synopsis = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    tagline = models.TextField(blank=True)
    recommended_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='books_recommended')

    class Meta:
        ordering = ["-added_on"]

    def __str__(self):
        return f"{self.title} | by {self.author}"


class Review(models.Model):
    """
    Stores a single review related to :model: `auth.User`
    and :model: `catalogue.Book`
    """
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviewer")
    title = models.CharField(max_length=200)
    body = models.TextField()
    rating = models.IntegerField(choices=RATING)
    added_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-added_on"]

    def __str__(self):
        return f"{self.rating} stars for {self.book.title} | reviewed by {self.reviewer}"
