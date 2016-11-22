from django import forms


class PlaneForm(forms.Form):
    manufacturer = forms.CharField(required=False)
    model = forms.CharField(required=False)
    page = forms.IntegerField(required=False, widget=forms.HiddenInput())
