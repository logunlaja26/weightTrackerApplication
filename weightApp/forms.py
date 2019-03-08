from django import forms
from weightApp.models import userWeight

class weightForm(forms.ModelForm):
    class Meta():
        model = userWeight
        fields = '__all__'
