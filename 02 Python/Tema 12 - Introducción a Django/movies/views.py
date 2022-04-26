# from django.shortcuts import render

from django.views import generic

from .models import Director, Movie


class IndexView(generic.ListView):
    template_name = "directors.html"
    model = Director


class DirectorView(generic.DetailView):
    template_name = "director.html"
    model = Director


class MovieView(generic.DetailView):
    template_name = "movie.html"
    model = Movie
