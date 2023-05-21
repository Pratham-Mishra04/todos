from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Userdata
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
import datetime

def landing_page(response):
    return render(response,"ToDos2.html")

def items(request):
    set=Userdata.objects.filter(user=request.user)
    date_today=datetime.date.today()
    time_now=datetime.datetime.now().time()
    for item in set:
        if item.status!="Completed":
            if date_today>item.due_date:
                item.box_status="due"
                item.save()
            elif date_today==item.due_date:
                if time_now>item.due_time:
                    item.box_status="due"
                    item.save()
            else:
                item.box_status="light"
                item.save()
    items={"items":set}
    return render(request,"items.html",items)

def signin(response):
    return render(response, "signup.html")

def log_in(response):
    return render(response,"signin2.html")

def acc_created(request):
    if request.method=="POST":
        fname=request.POST.get('fname','')
        lname=request.POST.get('lname','')
        username=request.POST.get('username','')
        email=request.POST.get('email','')
        password=request.POST.get('password','')
        user=User.objects.create_user(username,email,password)
        user.first_name=fname
        user.last_name=lname
        user.save()
        user=authenticate(request, username=username,password=password)
        login(request, user)
        return redirect('/')
    else:
        return HttpResponse("Error")

def handlelogin(request):
    if request.method=="POST":
        username=request.POST.get("username","")
        password=request.POST.get('password'," ")
        user=authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse("No user")
    else:
        return HttpResponse("Error")

def handlelogout(request):
    logout(request)
    return redirect('/')

def additem(request):
    if request.method=="POST":
        title=request.POST.get("title","")
        description=request.POST.get("description","")
        user=request.user
        due_date=request.POST.get("date","")
        due_time=request.POST.get("time","")
        data=Userdata(user=user,title=title,description=description,status="Active",box_status="light", due_date=due_date,due_time=due_time)
        data.save()
        messages.success(request,"The TODO was added!")
        return redirect('/')
    else:
        return HttpResponse("Error")

def complete_item(request):
    set=Userdata.objects.filter(user=request.user)
    title=request.GET.get('title','')
    for item in set:
        if item.title==title:
            if item.box_status=="light":
                item.box_status="success"
                item.status="Completed"
            else:
                item.box_status="light"
                item.status="Active"
            item.save()
    return redirect('/items')  

def delete_item(request):
    set=Userdata.objects.filter(user=request.user)
    title=request.GET.get('title','none')
    print(title)
    for item in set:
        if item.title==title:
            item.delete()   
    return redirect('/items')

def profile(request):
    if request.method=='POST':
        user=request.user
        fname=request.POST.get('fname','')
        lname=request.POST.get('lname','')
        email=request.POST.get('email','')
        user.first_name=fname
        user.last_name=lname
        user.email=email
        user.save()
    set=Userdata.objects.filter(user=request.user)
    date_today=datetime.date.today()
    time_now=datetime.datetime.now().time()
    for item in set:
        if item.status!="Completed":
            if date_today>item.due_date:
                item.box_status="due"
                item.save()
            elif date_today==item.due_date:
                if time_now>item.due_time:
                    item.box_status="due"
                    item.save()
            else:
                item.box_status="light"
                item.save()
    items={"items":set}
    return render(request,"profile.html",items)

def edit_profile(request):
    set=Userdata.objects.filter(user=request.user)
    items={"items":set}
    return render(request,"edit_profile.html",items)