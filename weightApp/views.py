from django.shortcuts import render
from weightApp.forms import weightForm
from weightApp.models import userWeight
# Create your views here.

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
