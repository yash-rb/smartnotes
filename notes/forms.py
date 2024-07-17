from django import forms
from .models import Notes
from django.core.exceptions import ValidationError

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields= ('title', 'text')
        labels = {
            'text': "Write your thoughts here:"
        }
        widgets = {
                'title': forms.TextInput(attrs={'class':'from-control my-5'}),
                'text': forms.Textarea(attrs={'class':'form-control mb-5'})
        }
    
    def clean_title(self):
        title = self.cleaned_data['title']
        if 'django' not in title.lower():
            raise ValidationError('We only accept notes about django!')
        return title