from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from blog_app.models import category,post,comment
from blog.settings import MEDIA_ROOT, MEDIA_URL
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import CreateView,UpdateView,DeleteView
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.



def home(request):
    post = category.objects.all().order_by('-created_at')
    return render(request,'category.html',context={"post":post})





def details(request,cat):
    postd = post.objects.filter(related_cat=cat).order_by('-created_at')
    return render(request,'posts.html',context={"cat":cat,"postd":postd})





def postdetails(request,id):
    postd = get_object_or_404(post,pk=id)
    comments = comment.objects.filter(post=id)
    return render(request,'post.html',context={"postd":postd,"comments":comments})




class Addpost(CreateView):
    model = post
    template_name = 'newpost.html'
    fields = ('title','image','related_cat','tags')
    def form_valid(self, form):
        form.instance.auther = self.request.user
        return super().form_valid(form)






class Updatepost(UpdateView):
    model = post
    template_name = 'update_post.html'
    # fields = '__all__'
    fields = ('title','image','tags')
    success_url = f"/blog/home"




class Deletepost(DeleteView):
    model = post
    template_name = 'delete_post.html'
    fields = '__all__'
    success_url = f"/blog/home"
    



class Comment(CreateView):
    model = comment
    template_name = 'comment.html'
    # fields = '__all__'
    fields = ('message',)
    def form_valid(self, form):
        form.instance.auther = self.request.user
        postt = get_object_or_404(post,pk=self.kwargs['id'])
        form.instance.post = postt
        return super().form_valid(form)



class updatecom(UpdateView):
    model = comment
    template_name = 'updatecom.html'
    fields = ('message',)


class Deletecom(DeleteView):
    model = comment
    template_name = 'deletecom.html'
    success_url = f"/blog/home"





class Addcat(CreateView):
    model = category
    template_name = 'new_cat.html'
    fields = '__all__'
    success_url = f"/blog/home"



class Updatecat(UpdateView):
    model = category
    template_name = 'update_cat.html'
    # fields = '__all__'
    fields = ('cat_name','image','desc')
    success_url = f"/blog/home"


class Deletecat(DeleteView):
    model = category
    template_name = 'delete_cat.html'
    fields = '__all__'
    success_url = f"/blog/home"




def likeview(request,pk):
    # mpost = get_object_or_404(post, id=request.POST.get('post_id')) 
    # mpost.likes.add(request.user)
    return HttpResponseRedirect(reverse('post',args=[str(pk)]))
    





# def new_post(request):
#     cat = category.objects.all()
#     auther=User.objects.all()

#     if request.POST:
#         p = post()
#         p.title=request.POST["title"]
#         p.auther=request.POST["auther"]
#         p.tags=request.POST["tags"]
#         p.related_cat = request.POST["related_cat"]
#         timage=request.FILES["image"]

#         imgname = timage.name
#         file_system_storage = FileSystemStorage()
#         file_system_storage.save(f"blog_app/post/images/{imgname}",timage)
#         p.image= f"blog_app/post/images/{imgname}"
#         p.save()


#     return render(request,'newpost.html',context={"cat":cat,"auther":auther})

    