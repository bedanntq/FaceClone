from django.contrib import admin
from .models import Post,Comment,CustomUser
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'date_created', 'image')  # Các cột hiển thị trong Admin
    search_fields = ('content', 'author__username')  # Cho phép tìm kiếm
    list_filter = ('date_created',)  # Bộ lọc bên cạnh
@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','post', 'author')  # Các cột hiển thị trong Admin
    search_fields = ('content', 'author__username')  # Cho phép tìm kiếm
    list_filter = ('date_created',)  # Bộ lọc bên cạnh
@admin.register(CustomUser)
class PostAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email')  # Các cột hiển thị trong Admin