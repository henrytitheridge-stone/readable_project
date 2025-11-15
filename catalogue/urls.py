from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookList.as_view(), name='home'),
    # path('', views.homepage, name='home'),
    path('<slug:slug>/', views.book_detail, name='book_detail'),
]
