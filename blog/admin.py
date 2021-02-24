from django.contrib import admin
from .models import BlogProfile, BlogGallery, BlogMessage, BlogContact, BlogPost, BlogProject

# Register your models here.
admin.site.register(BlogProfile)
admin.site.register(BlogPost)
admin.site.register(BlogGallery)
admin.site.register(BlogMessage)
admin.site.register(BlogContact)
admin.site.register(BlogProject)