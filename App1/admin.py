from django.contrib import admin
from .models import BlogModels

# Register your models here.
@admin.register(BlogModels)
class AdminBlog(admin.ModelAdmin):
    list_display=['id','title','desc']

