from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class RegisterUser(forms.ModelForm):
    password = forms.CharField(min_length=5, required=True , label = "Parol:" ,widget = forms.PasswordInput(attrs={'class':'form-control'}))
    password_confirm = forms.CharField(min_length=5 , label = "Tekrar Parol:" ,widget = forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password','password_confirm']

    def __init__(self, *args, **kwargs):
        super(RegisterUser , self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
         
    
    def clean(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Parollar uygun gelmir!!")



    def clean_email(self):
        email = self.cleaned_data.get("email")
        email = email.lower()
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError("Bele bir email movcuddur")
        return email

    

class LoginUser(forms.Form):

    username = forms.CharField(required=True, label = "Username:",widget=forms.TextInput(attrs={'class':"form-control"}))
    password = forms.CharField(required=True, label= "Sefre:", widget= forms.PasswordInput(attrs={'class':'form-control'}))

    
        

            

       
 
 
       