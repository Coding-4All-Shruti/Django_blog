from django.http import HttpResponse
from django.shortcuts import render

from blogs.models import Category, blog


def home(request):
    # return HttpResponse('<h2> Homepage<h2>')

    ## fetching all the categories from the database and passing it to the home.html template
    categories = Category.objects.all()
    featured_post = blog.objects.filter(is_featured = True).order_by('updated_at')
    posts = blog.objects.filter(is_featured = False, status= 'Published')
    context = {
        'categories': categories,
        'featured_post': featured_post,
        'posts': posts
    }
    
    return render(request, 'home.html', context)
