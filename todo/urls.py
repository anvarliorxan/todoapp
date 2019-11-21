from django.urls import path
from . import views




urlpatterns = [
    path('',views.todo, name = "todo"),
    path('addtodo',views.addtodo,name = "addtodo"),
    path('addshare/<str:id>',views.addshare,name = "addshare"),
    path('share',views.todo_shared_with_me,name="share"),
    
    path('comment/<str:id>',views.addComment,name = "comment"),

    path('send',views.send,name="send"),
    path('delete/<str:id>',views.deletetodo,name = "delete"),
    path('detail/<str:id>',views.detail,name = "detail"),
    path('update/<str:id>',views.updateTodo,name = "update"),
]
