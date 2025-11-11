from django.shortcuts import render
from django.views import generic
from .models import Book


# Create your views here.
def homepage(request):

    recent_books = Book.objects.filter(status=1)[:3]

    return render(
        request, 
        "catalogue/index.html",	
        {"recent_books": recent_books,},
    )	



class BookList(generic.ListView):
    """
    Returns all published book entries in :model: `catalogue.Book`
    and displays them in a list

    **Context**
    ``queryset``
        All published instances of :model: `catalogue.Book`
    **Template**
        :template: `catalogue/book_list.html`
    """

    queryset = Book.objects.filter(status=1)
    template_name = "catalogue/book_list.html"
