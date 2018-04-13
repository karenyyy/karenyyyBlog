from django.contrib import admin
from .models import Post, Category, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
    list_filter = ('created_time', 'category', 'author')
    search_fields = ('title', 'body')


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
