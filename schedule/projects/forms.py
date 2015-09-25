from django import forms

from schedule.projects.models import Project

# forms
class ProjectForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = [
            'name',
            'type',
            'contract',
            'notes'
        ]        