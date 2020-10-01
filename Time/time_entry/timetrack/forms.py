from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TaskForm(forms.ModelForm):
    name= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Task title...'}), label=False)
    due= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Due date...'}), label=False)
    start= forms.DateTimeField(widget= forms.TextInput(attrs={'placeholder':'Start date..'}),label=False)
    end= forms.DateTimeField(widget= forms.TextInput(attrs={'placeholder':'End date...'}),label=False)
    project=forms.ModelChoiceField(queryset=Project.objects.all().order_by('name'))
    complete=forms.BooleanField(required=False) 
    
    class Meta:
        model = Task
        fields = ['name','start','end','due','project','complete']


class UpdateForm(forms.ModelForm):
    name= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Task title...'}))
    due= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Due date...'}), label=False)
    start= forms.DateTimeField(widget= forms.TextInput(attrs={'placeholder':'Start date..'}),label=False)
    end= forms.DateTimeField(widget= forms.TextInput(attrs={'placeholder':'End date...'}),label=False)
    project=forms.ModelChoiceField(queryset=Project.objects.all().order_by('name'))
    complete=forms.BooleanField(required=False)
    

    class Meta:
        model = Task
        fields = ['name','start','end','due','project','complete']        


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username','email','password1','password2']