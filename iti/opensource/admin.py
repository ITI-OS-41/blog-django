from django.contrib import admin
from .models import Post, Category


def custom_titled_filter(title):
    class Wrapper(admin.FieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance
    return Wrapper


class CustomPost(admin.ModelAdmin):
    fieldsets = (
        ['Post Information', {'fields': ['title','slug','author','content','status']}],
        ['Category Information', {'fields': ['category']}]
    )
    list_display = ('title', 'category', 'author', 'is_published')
    list_filter = (
        ('category__title', custom_titled_filter('category')),
        'status')
    search_fields = ['title', 'Category__title']

class InlinePost(admin.StackedInline):
    model = Post
    extra = 1

class CustomCategory(admin.ModelAdmin):
    inlines = [InlinePost]



admin.site.register(Post, CustomPost)
admin.site.register(Category, CustomCategory)




