import requests
from django.conf import settings
from django.shortcuts import render

def movie_gallery(request):
    url = f"https://api.themoviedb.org/3/movie/popular"
    params = {
        "api_key": settings.TMDB_API_KEY,
        "language": "en-US",
        "page": 1,
    }
    response = requests.get(url, params=params)
    movies = response.json().get('results', [])

    return render(request, 'gallery/gallery.html', {'movies': movies})
