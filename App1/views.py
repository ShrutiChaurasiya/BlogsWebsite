from django.shortcuts import render,redirect,HttpResponse
from .models import BlogModels


# Create your views here.
def home(request):
    blog_data = BlogModels.objects.all()
    context={"blog_data":blog_data}
    return render(request,"home.html",context)

def delete_blog(request,id):
    blog = BlogModels.objects.get(id = id)
    blog.delete()
    return redirect("Home")

def update(request,id):
    blog = BlogModels.objects.get(id= id)
    context = {'blog': blog}
    
    if request.method == 'POST':
        n_title = request.POST['title']
        n_desc = request.POST['desc']
        
        blog.title = n_title
        blog.desc = n_desc

        blog.save()
        return redirect('Home')
    return render(request,'update.html',context)

def addblog(request):

    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        
        if len(title)>=1 and len(desc)>=1:
            blog = BlogModels(title = title, desc = desc)
            blog.save()
            return redirect('Home')
        else:
            return redirect('Home')
    return render(request,'addblog.html')