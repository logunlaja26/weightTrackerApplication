from django.shortcuts import render, redirect
from weightApp.forms import weightForm
from weightApp.models import userWeight


def home(request):
    return render(request,'weightApp/home.html')

def weightdata(request):

    form = weightForm()

    if request.method == "POST":
        form = weightForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return home(request)
        else:
            print('ERROR FORM INVALID')

    context = {
        'form':form,
        'weight_records': userWeight.objects.all()
    }

    return render(request,'weightApp/weightdata.html',context)

def weightdata_edit(request):
    # filter the weight weight weight weight record
    # update the weight record
    # save the database

    form = weightForm()

    if request.method == "POST":
        form = weightForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return home(request)
        else:
            print('ERROR FORM INVALID')

    context = {
        'form':form,
        'weight_records': userWeight.objects.all()
    }

    return render(request,'weightApp/weightdata.html',context)
