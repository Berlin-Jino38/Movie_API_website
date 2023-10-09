from django.shortcuts import render,redirect
from .models import Movie,Movie_detail
from .forms import SignupForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index_view(request):
    movies = Movie.objects.all()
    return render (request, 'myApp/index.html', {'movies': movies})

def detail_view(request, name):
    if Movie.objects.filter(name=name).exists():
        movies = Movie_detail.objects.filter(movie__name=name)
        return render(request, 'myApp/details.html', {'movies': movies})

def search_view(request):
    query = request.GET.get('q')
   
    if query:
        items = Movie.objects.filter(name__icontains=query).order_by('-name')
       
    else:
        # Handle the case when 'q' is not provided, for example, display all categories.
        items = Movie.objects.all().order_by('-name')  
    return render(request, 'myApp/index.html', {'movies': items})


def signup_view(request):
    if request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            return redirect('/accounts/login/')

    else:
        form=SignupForm()
    return render(request, 'myApp/signup.html', {'form': form})