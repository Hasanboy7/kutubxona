from .models import Place
from django import forms
class FormPlaces(forms.ModelForm):
    name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': "form-control"}))
    description=forms.CharField(required=True,widget=forms.Textarea(attrs={'class': "form-control"}))
    addres=forms.CharField(required=True,widget=forms.TextInput(attrs={'class': "form-control"}))
    img=forms.ImageField(required=True,widget=forms.FileInput(attrs={'class': "form-control"}))

    class Meta:
        model=Place
        fields=['name','description','addres','img']

class FormAdd(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    description=forms.CharField(widget=forms.Textarea(attrs={'class': "form-control"}))
    addres=forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    img=forms.ImageField(widget=forms.FileInput(attrs={'class': "form-control"}))

    class Meta:
        model=Place
        fields=['name','description','addres','img']
        