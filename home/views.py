from django.shortcuts import get_object_or_404 , render, redirect
from django.contrib.auth.decorators import login_required
from .form import registrationForm,PostForm, CommentForm
from .models import Post,Comment
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json

# Create your views here.
def post_detail(request, post_id):
    post = get_object_or_404(Post, id = post_id)
    return render(request, 'page/post_detail.html', {'post': post})

def home(request):
    posts = Post.objects.all().order_by('-date_created')
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/')  # Chuyển hướng về trang gốc
    else:
        form = PostForm()
    return render(request, 'page/home.html', {'form': form, 'posts': posts})

@login_required(login_url='login')  # Yêu cầu đăng nhập, chuyển hướng đến trang đăng nhập nếu chưa đăng nhập
def add_comment(request, post_id):
    # if not request.user.is_authenticated:
    #     messages.error(request, "Vui lòng đăng nhập trước.")
    #     return redirect(reverse('login'))  # Chuyển hướng đến trang đăng nhập

    post = get_object_or_404(Post, id = post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect(f"{reverse('home')}")  # Chuyển hướng về trang gốc
    return redirect('page/post.html', {'form': form, 'post': post})
    
def register(request):
    form = registrationForm()
    if request.method=='POST':
        form = registrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'security/register.html', {'form': form})

def get_comments(request, post_id):
    comments = Comment.objects.filter(post_id = post_id).order_by('-date_created')
    comment_list = [
        {
        'id': comment.id,
        'author':comment.author.username,
        'content': comment.content,
        'date_created': comment.date_created.strftime('%Y-%m-%d %H:%M:%S')
        }
        for comment in comments
    ]
    return JsonResponse({'comments': comment_list})
    
    
def add_comment_test(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            post_id = data.get('post_id')
            content = data.get('content')
            user = request.user

            # Tìm bài viết
            post = Post.objects.get(id=post_id)

            # Tạo bình      
            new_comment = Comment.objects.create(post=post, author=user, content=content)

            # Trả về dữ liệu bình luận vừa tạo
            return JsonResponse({
                'success': True,
                'comment': {
                    'id': new_comment.id,
                    'author': user.username,
                    'content': new_comment.content,
                    'date_created': new_comment.date_created.strftime('%Y-%m-%d %H:%M:%S')
                }
            })
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})