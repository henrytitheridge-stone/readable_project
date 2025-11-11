from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))


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