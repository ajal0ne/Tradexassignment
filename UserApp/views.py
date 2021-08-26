from django.shortcuts import render,redirect
from . forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'index.html')

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post(
                user = request.user,
                text = request.POST['text'],
                created_at = request.POST['created_at'],
                updated_at = request.POST['updated_at']
                
            )
            post.save()
            messages.success(request,f'Post created {request.user.username}!!')
    else:
        form = PostForm()
    post = Post.objects.filter(user=request.user)

    context={'form':form }
    return render(request,'create_post.html',context)
