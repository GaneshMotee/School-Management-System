from django import forms
from .models import Gpm


class TaskForm(forms.ModelForm):
    class Meta:
        model = Gpm
        fields = ['school_name','school_id','teachers','students','school_address']
