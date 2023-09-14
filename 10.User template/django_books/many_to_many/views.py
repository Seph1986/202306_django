from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Author, Book


# Create your views here.
def index(request):

    context = {
        'books': Book.objects.all()
    }
    
    return render(request,'books/index.html', context)


def data_digest(request):

    if request.POST['hidden'] == 'book':
        print('----------BOOK------------')
        print(request.POST)


        title = request.POST['title']
        description = request.POST['description']

        Book.objects.create(title=title, desc=description)
        return redirect(reverse('index'))

    if request.POST['hidden'] == 'author':
        
        print('----------AUTHOR------------')
        print(request.POST)


        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        notes = request.POST['notes']

        Author.objects.create(first_name=first_name, last_name=last_name, notes=notes)
        return redirect(reverse('authors'))
    

def book_detail(request, id):

    book = Book.objects.get(id=id)
    authors = book.authors.all()
    dont_authors = Author.objects.exclude(id__in=[autor.id for autor in authors])

    context = {
        'book': book,
        'authors': authors,
        'to_add_authors': dont_authors,
    }


    return render(request, 'books/detail.html', context)

def add_author_to_book(request, id):

    book_instance = Book.objects.get(id=id)
    author_id = request.POST['author_data']
    
    book_instance.authors.add(author_id)

    return redirect(reverse('book_detail', kwargs={'id':id}))


def authors(request):

    context = {
        'authors': Author.objects.all()
    }

    return render(request, 'authors/index.html',context)


def author_detail(request, id):

    author = Author.objects.get(id=id)
    books = author.books.all()
    dont_books = Book.objects.exclude(id__in=[book.id for book in books])

    context = {
        'author': author,
        'books': books,
        'to_add_books': dont_books,
    }


    return render(request, 'authors/detail.html', context)


def add_book_to_author(request, id):

    author_instance = Author.objects.get(id=id)
    book_id = request.POST['book_data']
    
    author_instance.books.add(book_id)

    return redirect(reverse('author_detail', kwargs={'id':id}))