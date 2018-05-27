from django import forms
from .models import Produtos


class ProdutoForm(forms.Form):
    categoria = forms.ChoiceField(choices=Produtos)
