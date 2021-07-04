from django import forms

class Egc(forms.Form):
    egcheader = forms.FileField(label='EGC Header')
    egcdata = forms.FileField(label='EGC Data')