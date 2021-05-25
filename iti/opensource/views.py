from django.core import paginator
from opensource.forms import CommentForm
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from opensource.models import Post, Category

from django.core.paginator import Paginator

#! Email imports 
from django.core.mail import send_mail

# Create your views here.

def getPost(request, pk): 
    post = Post.objects.get(id=pk)
    
    # ! START:  Check comment form request 
    commentForm = CommentForm()
    if request.method == 'POST':
        commentForm = CommentForm(request.POST)
        commentForm.instance.name = request.user
        commentForm.instance.post = post

        if commentForm.is_valid():
            commentForm.save()
            return HttpResponseRedirect('/post/'+str(pk))
    # ! END: Check comment form request 

    # ! START: Like
    isLiked = post.likes.filter(id=request.user.id).exists()
    # ! END: Like 
    


    context = {'commentForm': commentForm,'post': post, 'isLiked': isLiked}

    return render(request, 'opensource/post.html', context)

def getAllPosts(request): 
    posts = Post.objects.all()
    p = Paginator(posts,4)
    page_num = request.GET.get('page',1)
    page = p.page(page_num)
    # ordering = ['-date_posted']
    # paginate_by = 5

    context = {'posts': page}
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
    
def likePost(request, pk): 
    post = get_object_or_404(Post,id=request.POST.get('post_id'))

    isLiked = post.likes.filter(id=request.user.id).exists()
    if isLiked:
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    
    return HttpResponseRedirect(reverse('post',args=[str(pk)]))

def subscribeCategory(request, pk): 
    category = get_object_or_404(Category,id=request.POST.get('category_id'))
    
    isSubscribed = category.subscribers.filter(id=request.user.id).exists()
    if isSubscribed:
        category.subscribers.remove(request.user)
        #!-- email
       
    else:
        category.subscribers.add(request.user)
        send_mail(
            'subscription Notification ' , #subject
            'you have subscribed to ' + category.title + ' Category', #msg
            # 'omnia.soliman.m@gmail.com', #from
            '', #from
            [request.user.email], #to 
            # ['omnia.soliman.m@gmail.com'], #to 
            )

    
    return HttpResponseRedirect(reverse('posts'))
