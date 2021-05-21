from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

from ckeditor.fields import RichTextField


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title


#  Post status 
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    # content =  models.CharField(max_length=1000)
    content = RichTextField(blank=True, null=True)

    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    # tags = TaggableManager()
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def save(self, *args, **kwargs):
        if self.slug == None or not self.slug or self.slug == '':
            self.slug = slugify(self.title)
            super(Post, self).save(*args, **kwargs)


    class Meta:
        ordering = ['-created_on'] 

    def __str__(self):
        return self.title
        
    def is_published(self):
        return self.status == True
    is_published.boolean = True
