from unicodedata import name
from django.urls import path
from blog_app.views import home,details,Addpost,postdetails,Updatepost,Deletepost,Comment,Addcat,Updatecat,Deletecat,updatecom,Deletecom,likeview


urlpatterns = [
    path("home/",home,name='home'),
    path("catigory/<str:cat>",details,name="details"),
    path("post/<int:id>",postdetails,name="post"),
    path("post/<int:pk>/update",Updatepost.as_view(),name="update_post"),
    path("cat/<int:pk>/update",Updatecat.as_view(),name="update_cat"),
    path("post/<int:pk>/delete",Deletepost.as_view(),name="Delete_post"),
    path("cat/<int:pk>/delete",Deletecat.as_view(),name="Delete_cat"),
    path("post/new",Addpost.as_view(),name="new_post"),
    path("cat/new",Addcat.as_view(),name="new_cat"),
    path("comment/<int:id>",Comment.as_view(),name="comment"),
    path("comment/<int:pk>/update",updatecom.as_view(),name="update_com"),
    path("comment/<int:pk>/delete",Deletecom.as_view(),name="Delete_com"),
    path("like/<int:pk>",likeview,name='like_post'),
]