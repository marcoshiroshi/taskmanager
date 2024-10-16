from django import forms
from django.core.exceptions import ValidationError
from task.models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'required': True}),
        }

        fields = [
            'description',
        ]