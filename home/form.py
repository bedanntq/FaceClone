import re
from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class registrationForm(forms.Form):
    username = forms.CharField(label='Tài khoản',max_length=20)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Nhập mật khẩu', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Nhập lại mật khẩu', widget=forms.PasswordInput())
    
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError("Mật Khẩu Không Hợp Lệ")
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("Tài Khoản có ký tự đặc biệt")
        try:
            User.objects.get(username = username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("Tài Khoản Đã Tồn Tại!!!!")
    def save(self):
        User.objects.create_user(username = self.cleaned_data['username'],email = self.cleaned_data['email'],password=self.cleaned_data['password1'])

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image']
        
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['content']