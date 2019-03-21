import datetime
from django import forms
from weightApp.models import userWeight


def last_years():
    first_year = datetime.datetime.now().year - 6
    return list(range(first_year + 6, first_year, -1))

class weightForm(forms.ModelForm):
    entry_date = forms.DateField(widget=forms.SelectDateWidget(years = last_years()))
    class Meta():
        model = userWeight
        fields = '__all__'
