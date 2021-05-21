from opensource.forms import PostForm
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from opensource.models import Post, Category




# Create your views here.

def getPost(request, postId): 
    post = Post.objects.get(id=postId)
    context = {'post': post}
    return render(request, 'opensource/post.html', context)

def getAllPosts(request): 
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'opensource/posts.html', context)


def newPost(request): 
    postForm = PostForm()
    if request.method == 'POST':
        postForm = PostForm(request.POST)
        if postForm.is_valid():
            postForm.save()
            return HttpResponseRedirect('/opensource/all')
    context = {'postForm': postForm}
    return render(request, 'opensource/newPost.html', context)



def editPost(request, postId): 
    post = Post.objects.get(id = postId)
    postForm = PostForm(instance = post)

    if( request.method == 'POST'):
        postForm = PostForm(request.POST, instance=post)
        if postForm.is_valid():
            postForm.save()
             
    context = {'postForm': postForm}
    return render(request, 'opensource/newPost.html', context)

def deletePost(request, postId): 
    post = Post.objects.get(id = postId)
    post.delete()
    return HttpResponseRedirect('/opensource/all')
    