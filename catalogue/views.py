from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Book, Recommendation, Review
from .forms import RecommendationForm
from .forms import ReviewForm


class BookList(generic.ListView):
    """
    Returns all published book entries in :model: `catalogue.Book`
    and displays them in a list

    **Context**
    ``queryset``
        All published instances of :model: `catalogue.Book`
    **Template**
        :template: `catalogue/index.html`
    """

    queryset = Book.objects.filter(status=1)
    template_name = "catalogue/index.html"


def book_detail(request, slug):
    """
    Display an individual :model:`catalogue.Book`.

    **Context**
    ``book``
        An instance of :model:`catalogue.Book`.
    ``reviews``
        All approved reviews related to the book.
    ``review_count``
        A count of approved reviews related to the book.
    ``review_form``
        An instance of :form: `catalogue.ReviewForm`.

    **Template:**
    :template:`catalogue/book_detail.html`
    """

    queryset = Book.objects.filter(status=1)
    book = get_object_or_404(queryset, slug=slug)
    reviews = book.reviews.all().order_by("-added_on")
    review_count = book.reviews.filter(approved=True).count()

    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.reviewer = request.user
            review.book = book
            review.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Review submitted and awaiting approval'
            )

    review_form = ReviewForm()

    return render(
        request,
        "catalogue/book_detail.html",
        {"book": book,
         "reviews": reviews,
         "review_count": review_count,
         "review_form": review_form},
    )


def review_edit(request, slug, review_id):
    """
    Display an individual review to edit.

    **Context**
    ``book``
        An instance of :model: `catalogue.Book`.
    ``review``
        A single review related to the book.
    ``review_form``
        An instance of :form: `catalogue.ReviewForm`
    """
    if request.method == "POST":
        queryset = Book.objects.filter(status=1)
        book = get_object_or_404(queryset, slug=slug)
        review = get_object_or_404(Review, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid() and review.reviewer == request.user:
            review = review_form.save(commit=False)
            review.book = book
            review.approved = False
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating review.')

    return HttpResponseRedirect(reverse('book_detail', args=[slug]))


def review_delete(request, slug, review_id):
    """
    Delete an individual review.

    **Context**
    ``book``
        An instance of :model: `catalogue.Book`.
    ``review``
        A single review related to the book.
    """
    queryset = Book.objects.filter(status=1)
    book = get_object_or_404(queryset, slug=slug)
    review = get_object_or_404(Review, pk=review_id)

    if review.reviewer == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own reviews!')

    return HttpResponseRedirect(reverse('book_detail', args=[slug]))


def contact(request):
    """
    Displays a form related to :model: `catalogue.Recommendation` for users to
    recommend a book.
    
    **Context**
    ``recommendation_form``
        An instance of :form: `catalogue.RecommendationForm`.
    **Template**
    :template: `catalogue/contact.html`
    """

    if request.method == "POST":
        recommendation_form = RecommendationForm(data=request.POST)
        if recommendation_form.is_valid():
            recommendation_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Recommendation received! '
                'I endeavour to respond within 2 working days.'
            )

    recommendation_form = RecommendationForm()

    return render(
        request,
        "catalogue/contact.html",
        {"recommendation_form": recommendation_form},
    )