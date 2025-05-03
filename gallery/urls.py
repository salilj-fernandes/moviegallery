from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_gallery, name='movie_gallery'),
]
