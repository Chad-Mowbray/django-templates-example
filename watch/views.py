from django.shortcuts import render
from .models import Movie

def list_movies(request):
    movies = Movie.objects.all()
    context = {
        "movies": movies
    }
    return render(request, 'watch/list_movies.html', context)