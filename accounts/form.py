from django import forms
from .models import SignupModel


class AccountForm(forms.ModelForm):

    class Meta:
        model = SignupModel
        widgets = {
            'password': forms.PasswordInput(),
        }
