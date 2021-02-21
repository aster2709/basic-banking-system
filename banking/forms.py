from django import forms
from .models import Customer
from django.forms import ModelForm


class FromForm(forms.Form):
    CHOICES = [('none','select')]
    for i, j in enumerate(Customer.objects.all()):
        CHOICES.append((i, j.name))
    name1 = forms.ChoiceField(label='From', initial='none', choices=CHOICES)

class AmountForm(forms.Form):
    amount = forms.IntegerField(label='Enter Amount')

class ToForm(forms.Form):
    CHOICES = [('none','select')]
    for i, j in enumerate(Customer.objects.all()):
        CHOICES.append((i, j.name))
    name2 = forms.ChoiceField(label='To', initial='none', choices=CHOICES)
