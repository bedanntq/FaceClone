from django.conf import settings
from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=255, blank=True, null=False, default='Bài Viết')
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Trỏ đến model người dùng
        on_delete=models.CASCADE,  # Xóa bài viết nếu người dùng bị xóa
        related_name='posts',      # Tên quan hệ ngược
    )
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)  # Trường ảnh

    def __str__(self):
        return f"{self.title} by {self.author.username}"
    
class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
