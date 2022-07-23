from email import message
from django.db import models
from django.core.validators import MinValueValidator , MaxValueValidator
from django.urls import reverse 
from django.contrib.auth.models import User
# Create your models here.


class category(models.Model):
    cat_name   = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    desc       = models.CharField(max_length=1000,default="")
    image      = models.ImageField(upload_to="blog_app/category/images",null=True)



    def __str__(self) -> str:
        return self.cat_name




class post(models.Model):
    title        = models.CharField(max_length=200)
    auther       = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    image        = models.ImageField(upload_to="blog_app/post/images",null=True)
    related_cat  = models.ForeignKey(category,null=True,default=1,on_delete=models.CASCADE,related_name="cat_post")
    tags         = models.CharField(max_length=200)
    created_at   = models.DateTimeField(auto_now_add=True,null=True)
    likes        = models.ManyToManyField(User,related_name='blog_posts')



    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('home')



class comment(models.Model):
    message      = models.TextField(max_length=10000,default="")
    post         = models.ForeignKey(post,related_name="comments" ,on_delete=models.CASCADE)
    auther       = models.ForeignKey(User,related_name="comments" ,on_delete=models.CASCADE)
    created_at   = models.DateTimeField(auto_now_add=True,null=True)


    def __str__(self) -> str:
        return self.message


    def get_absolute_url(self):
        return f"/blog/post/{self.post.id}"


