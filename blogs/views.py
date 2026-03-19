from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import blog, Category, Comment
from django.shortcuts import get_object_or_404

from django.db.models import Q

# Create your views here.


def posts_by_category(request, category_id):
    posts = blog.objects.filter(status='Published', category_id=category_id)
    try:
        category = Category.objects.get(pk=category_id)
    except:
        # Redirect to home page if category does not exist
        return redirect('home')
    
    ## use get_object_or_404 when we need to show 404 error
    ## category = get_object_or_404(Category, pk=category_id)
    
    context = {
        'posts': posts,
        'category': category

    }

    return render(request, 'posts_by_category.html', context)




def blogs(request, slug):

    single_blog = get_object_or_404(blog, slug=slug, status='Published')

    if request.method=='POST':
        comment = Comment()
        comment.user = request.user
        comment.blog= single_blog
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)



    ##comment
    comments = Comment.objects.filter(blog=single_blog)
    comment_count = comments.count()

    context = {
        'single_blog': single_blog,
        'comments': comments,
        'comment_count': comment_count,
    }

    return render (request, 'blogs.html', context)


def search(request):

    keyword = request.GET.get('keyword')
    blogs = blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='Published')
    context ={
        'blogs': blogs,
        'keyword': keyword,
    }
    return render(request, 'search.html', context)






