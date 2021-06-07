from django.core import paginator
from opensource.forms import CommentForm,PostForm
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from opensource.models import Post, Category, User, Subscribtion, Comment

from django.core.paginator import Paginator
from taggit.models import Tag

import json 

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
            #! reply
            try:
                parent_id = request.POST.get('parent_id')
                parent_qs = Comment.objects.filter(id=parent_id)
                parent_obj = parent_qs.first()
                commentForm.instance.parent=parent_obj

            except Exception as e:
                print(e)

            # commentForm.
            commentForm.save()
            # return HttpResponseRedirect(context)
            return HttpResponseRedirect('/post/'+str(pk))
    # ! END: Check comment form request 

    # ! START: Like
    isLiked = post.likes.filter(id=request.user.id).exists()
    # ! END: Like 
    
    comments = list(post.comments.all().values())
    filteredComments = []
    for comment in (comments):
        comment['user'] = User.objects.filter(id=comment['name_id']).values()[0]
        print(comment['user'])
        if comment['parent_id'] == None:
            children = []
            for c in (comments):
                # ! is a child for this comment
                if c['parent_id'] == comment['id']:
                    children.append(c)
                    print(c)
            comment['children'] = children
            filteredComments.append(comment)

    context = {'commentForm': commentForm,'post': post, 'isLiked': isLiked, 'comments':filteredComments}
 
    return render(request, 'opensource/post.html', context)

def getAllPosts(request): 
    if request.user.id:
        subscribtions = Subscribtion.objects.filter(user=request.user.id).values_list('category_id', flat=True)

        posts = Post.objects.filter(category_id__in=subscribtions)
    else:
        posts = Post.objects.all()

    p = Paginator(posts,4)
    page_num = request.GET.get('page',1)
    page = p.page(page_num)
    # ordering = ['-date_posted']
    # paginate_by = 5

    context = {'posts': page, 'pageHeader': "All Posts"}
    return render(request, 'opensource/posts.html', context)

def newPost(request): 
    postForm = PostForm()
    if request.method == 'POST':
        postForm = PostForm(request.POST)
        if postForm.is_valid():
            # 
            obj = postForm.save(commit=False)
            obj.user = request.user
            obj.save()
            # postForm.save()
            # to save tags
            postForm.save_m2m()

            return HttpResponseRedirect('/opensource/all')
    context = {'postForm': postForm}

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

# filter tags
def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'posts':posts,
        'pageHeader': "Posts for tag: "+tag.name
    }
    return render(request, 'opensource/posts.html', context)
# filter categories
def category(request, pk):
    category = get_object_or_404(Category, id=pk)
    posts = Post.objects.filter(category=category)
    context = {
        'category':category,
        'posts':posts, 
        'pageHeader': "Posts for category: "+category.title
    }
    return render(request, 'opensource/posts.html', context)

# ! Search 
def search(request):
        # search.html,  searched -> da el name bta3 el input
    if request.method == 'POST':
        searched = request.POST['searched']
        posts = Post.objects.filter(title__contains=searched)
        return render(request, 'opensource/search.html',
        {'searched':searched,
        'posts':posts}) # -> we will pass it back to the page itself 

    else:
        return render(request, 'opensource/search.html',{})
    

def error_404(request,exception):
    return render(request, 'opensource/404.html')

