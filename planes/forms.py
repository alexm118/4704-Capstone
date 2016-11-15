from django import forms
from planes.models import Manufacturer, Plane, Helicopter


class PlaneForm(forms.ModelForm):
    manufacturer = forms.ModelChoiceField(queryset=Manufacturer.objects.all())

    class Meta:
        model = Plane
        exclude = ('engines', 'model')


class HeliForm(forms.ModelForm):
    manufacturer = forms.ModelChoiceField(queryset=Manufacturer.objects.all())

    class Meta:
        model = Helicopter
        exclude = ('engines', 'model')