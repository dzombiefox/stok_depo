from django import forms
from .models import Stok

class StokForm(forms.ModelForm):
    class Meta :
        model =Stok
        fields=["tanggal","kita","picasso","harmony","atena","size"]