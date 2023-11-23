from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Movie
from . forms import MovieForm


# Create your views here.
def index(request):
    movie=Movie.objects.all()
    context={
        'movie_list': movie

    }
    return render(request,'index.html',context)
def detail(request,movie_id):
    m=Movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':m})
def add_movie(request):
    if request.method=='POST':
        n=request.POST.get('name')
        d=request.POST.get('desc')
        y=request.POST.get('year')
        i=request.FILES['img']
        movie=Movie(name=n,desc=d,year=y,img=i)
        movie.save()
    return render(request,'add.html')

def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})

def delete(request,id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
