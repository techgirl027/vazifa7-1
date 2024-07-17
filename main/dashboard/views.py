# blog create
# blog update
# blog delete
from main import models
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from main.decorators import isOwner


@login_required(login_url="index")
def blog_create(request):
    if request.method == "POST":
        models.Blog.objects.create(
            author=request.user,
            title=request.POST["title"],
            body=request.POST["body"],
            image=request.FILES["image"],
        )
        return redirect("index")
    return render(request, "dashboard/create-blog.html")


@login_required
@isOwner(models.Blog)
def blog_update(request, id):
    blog = models.Blog.objects.get(id=id)
    if request.method == "POST":
        blog.title = request.POST["title"]
        blog.body = request.POST["body"]
        # blog.image = request.FILES['image']
        blog.save()
    return render(request, "dashboard/update-blog.html", {"blog": blog})


@login_required
@isOwner(models.Blog)
def blog_delete(request, id):
    models.Blog.objects.get(id=id).delete()
    return redirect("index")


@login_required
def my_blogs(request):
    blogs = models.Blog.objects.filter(author=request.user)
    return render(request, "dashboard/list-blogs.html", {"blogs": blogs})
