from django import forms
from .models import Recommendation, Review


class ReviewForm(forms.ModelForm):
    """
    Form class for authenticated users to leave a review on a book_detail page
    """
    class Meta:
        """
        Specify the django model and order of the fields
        """
        model = Review
        fields = ('title', 'rating', 'body')


class RecommendationForm(forms.ModelForm):
    """
    Form class for users to suggest a book be added to the database
    """
    class Meta:
        """
        Specify the django model and order of the fields
        """
        model = Recommendation
        fields = ('name', 'email', 'book_title', 'book_author',
                  'book_synopsis')
