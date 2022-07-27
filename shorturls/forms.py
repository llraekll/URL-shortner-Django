from tkinter import Label
from django import forms


class Url(forms.Form):
    url = forms.CharField(label="URL")
