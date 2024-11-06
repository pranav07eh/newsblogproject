from django.contrib import admin

# Register your models here.
from .models import Blog

@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    list_display=['title']