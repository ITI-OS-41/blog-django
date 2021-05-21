from django.contrib import admin
from .models import Post, Category


class CustomPost(admin.ModelAdmin):
    fieldsets = (
        ['Post Information', {'fields': ['title','author','status']}],
        ['Category Information', {'fields': ['category']}]
    )
    list_display = ('title', 'category', 'author', 'is_published')
    list_filter = ['category', 'title']
    search_fields = ['title', 'Category__title']

class InlinePost(admin.StackedInline):
    model = Post
    extra = 1

class CustomCategory(admin.ModelAdmin):
    inlines = [InlinePost]



admin.site.register(Post, CustomPost)
admin.site.register(Category, CustomCategory)

