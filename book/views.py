from django.shortcuts import render
from django.views import View
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404

from . import forms
from .models import Book


class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        book_name = request.GET.get('book_name')
        author_surname = request.GET.get('author_surname')
        sorting = request.GET.get('sorting')

        if book_name:
            books = books.filter(name__contains=book_name)

        if author_surname:
            books = books.filter(authors__surname__contains=author_surname)

        if sorting:
            books = books.order_by(sorting)

        return render(request, 'book/book_list.html', context={'books': books})


class BookDetailView(View):
    def get(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        authors = book.authors.all()
        return render(request, 'book/book_detail.html', context={'book': book, 'authors': authors})


class BookByAuthorView(View):
    def get(self, request, author_id):
        all_books = Book.objects.filter(authors__id=author_id)
        return render(request, 'book/book_list.html', context={'books': all_books})


class BookUnorderedListView(View):
    def get(self, request):
        books = Book.objects.filter(order=None)
        return render(request, 'book/book_unordered_list.html', context={'books': books})


class UserBookList(View):
    def get(self, request, user_id):
        books = Book.objects.filter(order__user=user_id)
        return render(request, 'book/user_book_list.html', context={'books': books})


class CreateBookView(View):
    def get(self, request):
        form = forms.CreateBookForm(request.GET)
        return render(request, 'book/create_book.html', context={'form': form})

    def post(self, request):
        form = forms.CreateBookForm(request.POST)
        if form.is_valid():
            return render(request, 'book/create_book.html', context={'form': form})
        return HttpResponseBadRequest('Bad Request')
