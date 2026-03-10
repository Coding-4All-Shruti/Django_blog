from django.contrib import admin

# Register your models here.
from .models import About, SocialLink


class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Check if there are any existing About instances
        if About.objects.exists():
            return False  # Disable the add permission if an instance already exists
        return True  # Allow adding if no instances exist


admin.site.register(About, AboutAdmin)

admin.site.register(SocialLink)