from django.http import HttpResponse
from django.shortcuts import redirect, render

from blogs.models import Category, blog
from assignments.models import About
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


def home(request):
    # return HttpResponse('<h2> Homepage<h2>')

    ## fetching all the categories from the database and passing it to the home.html template
    categories = Category.objects.all()
    featured_post = blog.objects.filter(is_featured = True).order_by('updated_at')
    posts = blog.objects.filter(is_featured = False, status= 'Published')

    abouts = About.objects.all()

    context = {
        'categories': categories,
        'featured_post': featured_post,
        'posts': posts,
        'abouts': abouts
    }
    
    return render(request, 'home.html', context)


def register(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            print(form.errors)
        

    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)



def login(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('home')
            
    form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'login.html', context)





def logout(request):
    auth.logout(request)
    return redirect('home')
