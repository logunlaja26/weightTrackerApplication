from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'weightApp/home.html')

def weightdata(request):
    return render(request,'weightApp/weightdata.html')
