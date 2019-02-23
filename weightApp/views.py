from django.shortcuts import render
from weightApp import forms
from weightApp.forms import weightForm

# Create your views here.

def home(request):
    return render(request,'weightApp/home.html')

def weightdata(request):

    form = weightForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return home(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'weightApp/weightdata.html',{'form':form})
