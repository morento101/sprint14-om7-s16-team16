from django.urls import path
from . import views

urlpatterns = [
    path('book_list/', views.BookListView.as_view(), name='book_list'),
    path('book_detail/<int:book_id>', views.BookDetailView.as_view(), name='book_detail'),
    path('book_by_author_id/<int:author_id>', views.BookByAuthorView.as_view(), name='book_by_author_id'),
    path('user_book_list/<int:user_id>', views.UserBookList.as_view(), name='user_book_list'),
    path('book_unordered_list/', views.BookUnorderedListView.as_view(), name='book_unordered_list'),
    path('create_book/', views.CreateBookView.as_view(), name='create_book'),
]
