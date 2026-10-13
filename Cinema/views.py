from django.shortcuts import render,redirect,get_list_or_404
from .models import *

def kino_list_view(request):
    kino = Kino.objects.all()
    return render(request,"home.html",context={"kino":kino})

def kino_create_view(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        time = request.POST.get("time")
        price = request.POST.get("price")
        age = request.POST.get("age")
        image = request.FILES.get("image")

        Kino.objects.create(title=title, description=description, time=time, price=price, age=age,image=image)
        return redirect("kino_list")
    return render(request,"create.html")

def kino_update_view(request,pk):
    kino = Kino.objects.get(id=pk)
    if request.method == "POST":
        kino.title = request.POST.get("title")
        kino.description = request.POST.get("description")
        kino.time = request.POST.get("time")
        kino.price = request.POST.get("price")
        kino.age = request.POST.get("age")
        if request.FILES.get("image"):
            kino.image = request.FILES.get("image")
        kino.save()

        return redirect("kino_list")
    return render(request,"update.html", context={"kino":kino})

def kino_dalete_view(request,pk):
    kino = Kino.objects.get(id=pk)
    if request.method == "POST":
        kino.delete()
        return redirect("kino_list")
    return render(request,"dalete.html",context={"kino":kino})


def feedback_create_view(request):
    if request.method == "POST":
        message = request.POST.get("message")
        Feedback.objects.create(message=message)
        return redirect("kino_list")
    return render(request,"feedback.html")




