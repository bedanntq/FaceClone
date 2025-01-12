from django.urls import path
from . import views
from .models import Post
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),  # Trang chính
    path('post/<int:post_id>/', views.post_detail, name = 'post_detail'),  # URL chi tiết bài viết
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='security/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]   