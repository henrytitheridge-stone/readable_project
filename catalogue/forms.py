from django import forms
from .models import Recommendation, Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('title', 'rating', 'body')


class RecommendationForm(forms.ModelForm):

    class Meta:
        model = Recommendation
        fields = ('name', 'email', 'book_title', 'book_author', 'book_synopsis')