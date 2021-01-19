from django import forms
from .models import Comment
from django import forms

from pagedown.widgets import PagedownWidget

from .models import Post
class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,widget=forms.Textarea)

    class Meta:
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),  # or whatever class you want to apply
            # and so on
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email','body')
