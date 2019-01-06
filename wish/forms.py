from django import forms
from .models import Wish


class NewWishForm(forms.ModelForm):
    class Meta:
        model = Wish
        fields = ['body']
