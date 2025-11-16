from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookList.as_view(), name='home'),
    path('contact/', views.contact, name='contact'),
    # path('', views.homepage, name='home'),
    path('<slug:slug>/', views.book_detail, name='book_detail'),
    path('<slug:slug>/edit_review/<int:review_id>', views.review_edit, name='review_edit'),
    path('<slug:slug>/delete_review/<int:review_id>', views.review_delete, name='review_delete'),
]
