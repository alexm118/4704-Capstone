from django import forms
from planes.models import Manufacturer, Plane, Helicopter


class PlaneForm(forms.ModelForm):
    manufacturer = forms.ModelChoiceField(queryset=Manufacturer.objects.all())
    model = forms.CharField(required=False)
    page = forms.IntegerField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = Plane
        exclude = ('engines', 'model')


class HeliForm(forms.ModelForm):
    manufacturer = forms.ModelChoiceField(queryset=Manufacturer.objects.all())
    model = forms.CharField(required=False)
    page = forms.IntegerField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = Helicopter
        exclude = ('engines', 'model')

