from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("message", "group")

        widgets = {
            'message':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }