from django import forms
from planes.models import Manufacturer, Plane


class PlaneForm(forms.ModelForm):
    manufacturer = forms.ModelChoiceField(queryset=Manufacturer.objects.all())

    class Meta:
        model = Plane
        exclude = ('engines', 'model')