from django.contrib import admin
from .models import Category, blog

### prepopulated slug

### blogs.model me agar title name bada hua to nhi ho payega isiliye isako handle karne ke liye prepopulated fields ka use karte hai taki title ke basis par slug automatic generate ho jaye
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':('title',)}

    """list_diplay is used to display the fields in the admin panel list """
    list_display = ('title', 'author', 'status', 'is_featured')
    search_fields = ('id', 'title', 'category__category_name', 'status')

    list_editable = ('is_featured',)


admin.site.register(Category)

admin.site.register(blog, BlogAdmin)