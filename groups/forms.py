from django import forms
from .models import Group

class UserForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ("name", "description")

        widgets = {
            'name':forms.TextInput(attrs={'class':'textinputclass'}),
            'description':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }