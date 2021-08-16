from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'auther', 'body')
        widget = {
            'title' : forms.TextInput(attrs= {'class':'form-control'}),
            'auther' : forms.Select(attrs= {'class':'form-control'}),
            'body' : forms.Textarea(attrs= {'class':'form-control'}),
        }