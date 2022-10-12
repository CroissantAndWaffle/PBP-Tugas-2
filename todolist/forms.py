from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        date = models.DateField()
        title = models.CharField(max_length=100)
        description = models.TextField()