from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<pk>", views.DirectorView.as_view(), name="director_list"),
    path("movie/<pk>", views.MovieView.as_view(), name="movie_list"),
]
