from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Book, Review
from .forms import ReviewForm


# Create your views here.
# def homepage(request):

#     recent_books = Book.objects.filter(status=1)[:3]

#     return render(
#         request, 
#         "catalogue/index.html",	
#         {"recent_books": recent_books,},
#     )	


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
