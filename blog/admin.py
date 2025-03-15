from django.contrib import admin
from .models import Post
from tags.models import Tag

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted')
    search_fields = ('title', 'content')
    list_filter = ('date_posted',)

@admin.register(Tag)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
