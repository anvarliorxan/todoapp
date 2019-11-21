from django.shortcuts import render,redirect
from .forms import RegisterUser,LoginUser
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages

def register(request):
    form = RegisterUser(request.POST or None)
    if form.is_valid():
        user = form.save(commit = False)
        password = form.cleaned_data.get("password")
        user.set_password(password)
        user.save()
        login(request,user)
        messages.success(request,"Tebrikler..Qeydiyyatdan kecdiniz")
        return redirect("todo")

    return render(request,"register.html",{"form":form})
    

def logoutUser(request):
    logout(request)
    messages.success(request,"Sistemden cixidiniz")
    return redirect("todo")


def loginUser(request):
    form = LoginUser(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)

        if user is None:
            messages.info(request,"Username ve yaxut parol sehfdir")
            return render(request,"login.html",{"form":form})

        messages.success(request,"Tebrikler Daxil oldunuz))")
        login(request,user)
        return redirect("todo")


    return render(request,"login.html",{"form":form})
