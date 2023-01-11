from django.shortcuts import render
from django.http import HttpResponse
from . models import *

# Create your views here.

def home(request):
       query = request.GET.get("title")
       all_movies = None
       if query:
        all_movies=movie.objects.filter(name__icontains=query)
       else:
         all_movies=movie.objects.all()
       context={ "movies":all_movies, }
       return render(request,"main/index.html",context)



def detail(request,id):
       single_movie=movie.objects.get(id=id)
       context={"m":single_movie,}
       return render(request,"main/detail.html",context)

def about_us(request):
       return render(request,"main/about_us.html")

def Lang (request, L):
       all_movies=movie.objects.filter(language=L)
       context={"movies":all_movies,}
       return render(request,"main/index.html",context)
