from django import forms
from .models import Todo,Share,Comment


class FormTodo(forms.ModelForm):
    
    class Meta:
        model = Todo
        fields = ["name","description","end_date"]



class FormShare(forms.ModelForm):
    
    class Meta:
        model = Share
        fields = ['todo','with_user']

    


    
class FormComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_author','comment_content']