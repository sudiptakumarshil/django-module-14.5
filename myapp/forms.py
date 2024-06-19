from django import forms
from django.forms.widgets import NumberInput
import datetime

STATUS = [
    ('1', 'Active'),
    ('0', 'Inactive')
]

class MyPracticeForm(forms.Form):
    title = forms.CharField(max_length = 100,label="Title")
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField(label="Manager Email")
    is_public = forms.BooleanField(label="Is Public")
    deadline = forms.DateField(widget=NumberInput(attrs={'type': 'date'}),initial=datetime.date.today)
    budget = forms.DecimalField(label="Project Budget")
    status = forms.ChoiceField(choices=STATUS,label="Status")