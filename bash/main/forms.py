from django.forms import ModelForm
from django import forms
from .models import ModelFile


# class UploadFileForm(ModelForm):
#     class Meta:
#         model = File
#         fields = ['image']


class UploadFileForm(forms.Form):
    about = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'Дополнительная информация'
    }), label='Дополнительная информация')


    file_source = forms.FileField(
        widget=forms.ClearableFileInput(attrs={
            'class':'d-none',
            'required': False
        }),
        required=False,
        # label="Файл для загрузки"
        label=""
    )


