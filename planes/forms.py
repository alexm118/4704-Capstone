from django import forms
from planes.models import Plane


class PlaneForm(forms.ModelForm):
    plane = Plane.objects.all().first()
    manufacturer = forms.ChoiceField(choices=plane.get_unique_manufacturers())

    class Meta:
        model = Plane
        exclude = ['model', 'engines']
