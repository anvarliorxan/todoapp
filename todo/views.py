from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from .models import Todo,Share,Comment
from .forms import FormTodo,FormShare
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .tasks import send_email_task
from django.contrib.auth.models import User
import datetime



@login_required(login_url ="user:login")
def todo(request):
    todo_list = Todo.objects.filter(author = request.user)
    context ={
        "todo_list":todo_list
    } 
    
    return render(request,"todo.html",context)
   

@login_required(login_url ="user:login")
def addtodo(request):
    form = FormTodo(request.POST or None)
    context ={"form":form}
    if form.is_valid():
        todo = form.save(commit= False)
        todo.author = request.user
        ten_minutes_before = todo.end_date - datetime.timedelta(minutes = 10)
        print("TEN MINS BEFORE:",ten_minutes_before)
        send_email_task.apply_async(countdown = 5)
        todo.save()
        messages.success(request,"Tapsiriq elave olundu))")
        
        return redirect("todo")
    
    return render(request,"addtodo.html",context)


@login_required(login_url ="user:login")
def deletetodo(request,id):
    todo = get_object_or_404(Todo,id = id,author = request.user)
    todo.delete()
    return redirect("todo")

@login_required(login_url ="user:login")
def detail(request,id):
    todo = get_object_or_404(Todo,id = id)
    comments = todo.comments.all()
    context = {
        "todo":todo,
        'comments':comments
    }
    return render(request,"detail.html",context)
 

@login_required(login_url ="user:login")
def updateTodo(request,id):
    todo = get_object_or_404(Todo,id = id,author = request.user)
    form = FormTodo(request.POST or None,instance = todo)
    if form.is_valid():
        todo = form.save(commit =False)
        todo.author = request.user
        todo.save()
        messages.success(request,"Tapsiriq deyisildi")
        return redirect("todo")

    else:
        return render(request,"update.html",{"form":form})


def send(request):
    send_email_task()
    return HttpResponse("salamlayiram")




@login_required(login_url ="user:login")
def addshare(request,id):
    
    form = FormShare(request.POST or None)
    form.fields["todo"].queryset = Todo.objects.filter(author = request.user)
    form.fields["with_user"].queryset = User.objects.all().exclude(pk=request.user.pk)
    if form.is_valid():
        form.save()
        messages.success(request,"tapsiriginizi paylasdiniz")
        return redirect("todo")
    return render(request,"share.html",{"form":form})



@login_required(login_url ="user:login")
def todo_shared_with_me(request):
    todo_list = Todo.objects.filter(share__with_user=request.user)
    context ={
        "todo_list":todo_list
    } 
    
    return render(request,"sharing.html",context)




def addComment(request,id):
    todo = get_object_or_404(Todo,id =id)
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content  =request.POST.get("comment_content")

        newComment = Comment(comment_author= comment_author ,comment_content= comment_content)
        newComment.comment_todo = todo
        newComment.save()
        messages.success(request,"Şərhiniz əlavə olundu)")
    return redirect('/detail/' +str(id))