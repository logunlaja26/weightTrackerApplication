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

    return render(request,'weightApp/weightdata.html',{'form':form})


def getWeight(request):
    weight_list = userWeight.objects.all()
    weight_dict = {'weight_records':weight_list}
    return render(request,'weightApp/weightdata.html',context=weight_dict)
