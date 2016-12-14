from django import forms
from planes.models import Manufacturer, Plane, Helicopter


class PlaneForm(forms.Form):
    manufacturer = forms.CharField(required=False)
    model = forms.CharField(required=False)
    page = forms.IntegerField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = Plane
        exclude = ('engines', 'model')


class HeliForm(forms.ModelForm):
    manufacturer = forms.ModelChoiceField(queryset=Manufacturer.objects.all())

    class Meta:
        model = Helicopter
        exclude = ('engines', 'model')