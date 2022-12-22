from .models import *
from django.forms import *

class MaxsulotForm(ModelForm):
    class Meta:
        model = Maxsulot
        fields = '__all__'
        # widjets={
        #     "name":TextInput(attrs={
        #         'class':'form-control',
        #         'placeholder':'Ismi'
        #     }),
        #     "telephone":TextInput(attrs={
        #         'class':'form-control',
        #         'placeholder':'Telefon raqam'
        #     }),
        #     "email": EmailInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Email',
        #     }),
        #     "comment": Textarea(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Murojaat matni',
        #     })
        # }