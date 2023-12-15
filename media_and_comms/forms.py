from django.forms import ModelForm
from django import forms
from .models import Comment, Reply

class CommentCreateForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'body']
        widgets = {
            'body' : forms.TextInput(attrs={'placeholder': 'Add comment ...'}),
            'author' : forms.TextInput(attrs={'placeholder': 'Your Name'})
        }
        labels = {
            'author': '',
            'body': ''
        }
        
        
class ReplyCreateForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['author', 'body']
        widgets = {
            'author' : forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'body' : forms.TextInput(attrs={'placeholder': 'Add reply ...', 'class': "!text-sm"})
        }
        labels = {
            'author': '',
            'body': ''
        }