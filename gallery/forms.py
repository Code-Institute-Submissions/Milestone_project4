from django import forms
from blog.models import comment

class post_comment(forms.ModelForm):
    class Meta:
        model=comment
        fields = ('content',)
        labels = {
             'content' : 'Your Comment'
        }
