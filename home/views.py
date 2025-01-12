from django.shortcuts import get_object_or_404 , render, redirect
from django.contrib.auth.decorators import login_required
from .form import registrationForm,PostForm, CommentForm
from .models import Post
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

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
