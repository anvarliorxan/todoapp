from django.db import models
from datetime import datetime
from django import forms
from django.shortcuts import get_object_or_404



class Todo(models.Model):

    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name="Istifadeci:")
    name = models.CharField(max_length=50 , verbose_name= "Tapsiriq adi:")
    description = models.TextField(max_length=3000  ,verbose_name= "Tesviri")
    created_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.name
    



class Share(models.Model):
	todo = models.ForeignKey('Todo', on_delete=models.CASCADE,verbose_name = "Paylasilacaq Tapsiriq")
	with_user = models.ForeignKey('auth.User', on_delete=models.CASCADE,verbose_name = "Kiminle")
    



class Comment(models.Model):
    comment_todo = models.ForeignKey('Todo',on_delete = models.CASCADE,verbose_name = "Tapşırıq",related_name = 'comments')
    comment_author = models.CharField(max_length=100 , verbose_name="Yazıçı")
    comment_content = models.CharField(max_length=600,verbose_name="Şərh")
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_content