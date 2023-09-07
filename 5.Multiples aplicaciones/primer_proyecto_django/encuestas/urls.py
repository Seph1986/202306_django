from django.urls import path     
from . import views

urlpatterns = [
    path('', views.encuestas),
    path('/nuevo', views.nuevo)
]