# k/myApp/forms.py
from django import forms

class CountryStateForm(forms.Form):
    country = forms.ChoiceField(choices=[], required=True)
    state = forms.ChoiceField(choices=[], required=True)