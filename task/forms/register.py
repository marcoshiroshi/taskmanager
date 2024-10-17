from django import forms
from task.models import Register


class RegisterForm(forms.ModelForm):

    class Meta:
        model = Register
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'required': True}),
            'minutes': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
        }

        fields = [
            'description',
            'minutes'
        ]