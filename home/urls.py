from django.urls import path
from . import views
from .models import Post
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),  # Trang chính
    path('post/<int:post_id>/', views.post_detail, name = 'post_detail'),  # URL chi tiết bài viết    
    path('add_comment_test/', views.add_comment_test, name='add_comment_test'),
    path('get_comments/<int:post_id>/', views.get_comments, name='get_comments'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='security/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]   