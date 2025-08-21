from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def movie_list(request):
    
    #Complex Query Result -> Python Dictionary ->JSon Response (because JSon work only work in dictionaries)
    movies = Movie.objects.all()
    print(movies.values()) #return dictionary
    data = {'movies': list(movies.values())}
    return JsonResponse(data)

def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    data = {
        'name' : movie.name,
        'description' : movie.description,
        'active' : movie.active
    }
    print(movie)
    return JsonResponse(data)