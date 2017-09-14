from django import forms
from home.models import Email


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ('email',)
