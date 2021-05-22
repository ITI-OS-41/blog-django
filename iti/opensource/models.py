from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify 
import re
import os

from urllib.parse import urlparse


# from ckeditor.fields import RichTextField


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

def sub_string(str,len):
    return str[0:len]

class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    # subscribers = models.ManyToManyField(User,related_name='subscribe', blank=True)  
    subscribers = models.ManyToManyField(User, through='Subscribtion')

    def __str__(self):
        return self.title

    # def total_subscribers(self):
    #     return self.subscribers.count()


#  Post status 
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


class Post(models.Model):
    image = models.ImageField(upload_to='iti/opensource/static/img', default='img/default.jpg')

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content =  models.CharField(max_length=1000,null=True)
    # content = RichTextField(blank=True, null=True)

    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    # tags = TaggableManager()
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    likes = models.ManyToManyField(User,related_name='posts', blank=True)

    def total_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        if len(self.slug) == 0:
            self.slug = slugify(self.title)
        else :
            self.slug = slugify(self.slug)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_on'] 

    def __str__(self):
        return self.title
        
    def is_published(self):
        return self.status == True
    is_published.boolean = True

    @property
    def brief_content(self):
        return sub_string(cleanhtml(self.content),20)+'...'

    def get_image(self):
        imgName = self.image.name.split('/')
        return 'img/'+imgName[-1]



class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name) 



class BadWord(models.Model):
    word = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.word 



class Subscribtion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subscribed_on = models.DateField(auto_now= True) 

    class Meta:
        unique_together = ('user', 'category')

    def __str__(self):
        return self.user.username+' - '+self.category.title
    
    def cat(self):
        return self.category.id
    
    def total_subscribers(self):
        return self.category.subscribers.count()
