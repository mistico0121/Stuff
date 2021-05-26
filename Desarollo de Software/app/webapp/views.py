# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from .models import *
from .forms import *


def image_upload(request):
    if request.method == "POST" and request.FILES["image_file"]:
        image_file = request.FILES["image_file"]
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        image_url = fs.url(filename)
        print(image_url)
        return render(request, "upload.html", {
            "image_url": image_url
        })
    return render(request, "upload.html")

def index(request):

    threads = Thread.objects.all()
    form = ThreadForm()

    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'threads':threads, 'form': form}
    return render(request, "board.html", context)

def thread_view(request, my_id):
    obj  = get_object_or_404(Thread, id = my_id)
    form = PostForm()
    posts = Post.objects.filter(thread_id = my_id)
    print("testeando print")
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        print("acaaa")
        if form.is_valid():
            test = form.save(commit = False)
            test.thread_id = my_id
            test.save()

        return redirect(f"{obj.get_absolute_url()}")

    context = {
        'obj' : obj,
        'form' : form,
        'posts' : posts
    }

    return render(request, "thread.html",context)