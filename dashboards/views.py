from django.shortcuts import get_object_or_404, redirect, render

from blogs.models import Category, blog
from django.contrib.auth.decorators import login_required

from .forms import BlogPostForm, CategoryForm
from django.template.defaultfilters import slugify





# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blog_count = blog.objects.all().count()
    context ={
        'category_count': category_count,
        'blog_count': blog_count,
    }
    return render(request, 'dashboard/dashboard.html', context)




def categories(request):
    return render(request, 'dashboard/categories.html')



def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
        
    forms = CategoryForm()
    context = {
        'forms': forms
    }
    return render(request, 'dashboard/add_category.html', context)



### edit category in category dashboard
def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=category)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/edit_category.html', context)




def delete_category(request,pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')




def posts(request):
    posts = blog.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'dashboard/posts.html', context)




def add_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False) ### temporarily save the form data to post variable without saving to database
            post.author = request.user
            post.save()
            title =form.cleaned_data['title']
            post.slug = slugify(title) + '-' + str(post.id)

            post.save()
            return redirect('posts')

        else:
            print(form.errors)

    forms = BlogPostForm()
    context = {
        'forms': forms,
    }
    return render(request, 'dashboard/add_post.html', context)





def edit_post(request,pk):
    post = get_object_or_404(blog, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title)+ '-'+ str(post.id)
            post.save()
            return redirect('posts')



    forms = BlogPostForm(instance=post)
    context = {
        'forms': forms, 
    }
    return render(request, 'dashboard/edit_post.html', context)



def delete_post(request, pk):
    post = get_object_or_404(blog,pk=pk)
    post.delete()
    return redirect('posts')