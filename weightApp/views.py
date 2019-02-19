from django.shortcuts import render
from weightApp import forms

# Create your views here.

def home(request):
    return render(request,'weightApp/home.html')

def weightdata(request):
    form = forms.weightForm()
    return render(request,'weightApp/weightdata.html',{'form':form})
