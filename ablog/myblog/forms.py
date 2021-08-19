from django import forms
from django.forms import Select
from .models import Post, Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'auther','category', 'body')
        choices = Category.objects.all().values_list('name','name')
        choice_list = []
        
        for i in choices:
            choice_list.append(i)


        widgets = {
            'category' : Select(choices = choice_list),
            'auther' : forms.TextInput(attrs = {'value':'','id': 'elder','type':'hidden'}),


            }
        # widget = {
        #       'title' : forms.TextInput(attrs= {'class':'form-control'}),
        #       'auther' : forms.Select(attrs= {'class':'form-control'}),
        #       'category' : forms.Select(choices = choices,attrs= {'class':'form-control'}),
        #       'body' : forms.Textarea(attrs= {'class':'form-control'}),
        #   }  