from django import forms
from weightApp.models import userWeight

class weightForm(forms.ModelForm):
    #date = forms.DateField()
    #weight = forms.IntegerField()
    class Meta():
        model = userWeight
        fields = '__all__'
