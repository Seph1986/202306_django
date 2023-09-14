from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('data/', views.data_digest, name='data_digest'),
    path('book/<int:id>/', views.book_detail, name='book_detail'),
    path('book/add_user/<int:id>/', views.add_author_to_book, name='add_author_to_book'),
    path('authors/', views.authors, name='authors'),
    path('authors/<int:id>/', views.author_detail, name='author_detail'),
    path('author/add_book/<int:id>/', views.add_book_to_author, name='add_book_to_author'),
]
