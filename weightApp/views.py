from django.shortcuts import render, redirect
from weightApp.forms import weightForm
from weightApp.models import userWeight
from datetime import datetime


def home(request):
    return render(request,'weightApp/home.html')

def weightdata(request):

    form = weightForm()

    if request.method == "POST":
        form = weightForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect('weightdata')
        else:
            print('ERROR FORM INVALID')


    context = {
        'form':form,
        'weight_records': userWeight.objects.all()
    }

    return render(request,'weightApp/weightdata.html',context)


def weightdata_edit(request):
    formData = request.POST

    if request.method == "POST":
        # filter the weight record
        weightEntry = userWeight.objects.filter(id=formData['id'])
        # update the weight record
        entry_date = datetime.strptime(formData['date'], '%m-%d-%Y')
        weightEntry.update(weight_entry=formData['weight'],entry_date = entry_date)

    return redirect('weightdata')

def weightdata_delete(request):
    formData = request.POST

    if request.method == "POST":
        userWeight.objects.filter(id=formData['id']).delete()

    return redirect('weightdata')
