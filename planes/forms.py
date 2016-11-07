from django import forms
from planes.models import Manufacturer, Plane


class PlaneForm(forms.ModelForm):
    manufacturer = forms.ModelChoiceField(queryset=Manufacturer.objects.all())
    page = forms.IntegerField(required=True, widget=forms.HiddenInput())

    class Meta:
        model = Plane
        exclude = ('engines', 'model')