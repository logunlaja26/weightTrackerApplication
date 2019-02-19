from django import forms

class weightForm(forms.Form):
    date = forms.DateField()
    weight = forms.IntegerField()
