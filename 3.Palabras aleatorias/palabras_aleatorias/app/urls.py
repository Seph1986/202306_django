from django.urls import path
from . import views

urlpatterns = [
    path('random_word', views.random_word),
    path('clear', views.clear)
]