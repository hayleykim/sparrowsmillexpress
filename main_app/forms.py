from django import forms
from .models import Menu


class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)



class MenuForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))
    note = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))

    class Meta:
        model = Menu
        fields = '__all__'
        exclude = ['user']

class PhotoUploadForm(forms.Form):
    photo_file = forms.ImageField()