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

    form = weightForm()

    if request.method == "POST":
        # filter the weight record
        weightEntry = userWeight.objects.filter(id=request.POST['id'])
        print(weightEntry)
        # update the weight record
        weightEntry.update(weight_entry=request.POST['weight'])
        # save the database

    context = {
        'form':form,
        'weight_records': userWeight.objects.all()
    }

    return redirect('weightdata')
