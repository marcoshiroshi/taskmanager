from django import forms
from task.models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'required': True}),
            'user': forms.Select(attrs={'class': 'form-select', 'required': True}),
        }

        fields = [
            'description',
            'user',
        ]