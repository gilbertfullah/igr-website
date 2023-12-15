from django import forms
from .models import News, Release, Podcast, Gallery, Events, Comment
from django.core.validators import RegexValidator
from ckeditor.widgets import CKEditorWidget


class ReleaseForm(forms.ModelForm):
    title = forms.CharField(label="Title", min_length=3, validators= [RegexValidator(r'^[a-zA-Z\s]*$', message="Only letter is allowed!")], 
                required=True, widget=forms.TextInput(attrs={'placeholder':'Title', 'style':'font-size: 13px; text-transform: capitalize'}))
    
    author = forms.CharField(label="Author", min_length=3, validators= [RegexValidator(r'^[a-zA-Z\s]*$', message="Only letter is allowed!")], 
                required=True, widget=forms.TextInput(attrs={'placeholder':'Author', 'style':'font-size: 13px; text-transform: capitalize'}))
    
    content = forms.CharField(label="Content", min_length=10, required=True, widget=CKEditorWidget())
    
    published_date = forms.DateField(label="Job Expiration Date", required=False, widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control datepicker-input'}))
    
    image = forms.FileField(label="Upload company logo", required=False, widget=forms.ClearableFileInput(attrs={'style':'font-size: 13px'}))
    
    document = forms.FileField(label="Document", required=False, widget=forms.ClearableFileInput(attrs={'style':'font-size: 13px'}))
    
    class Meta:
        model = Release
        fields = ['title', 'author', 'content', 'published_date', 'image', 'document']
        

class NewsForm(forms.ModelForm):
    title = forms.CharField(label="Title", min_length=3, validators= [RegexValidator(r'^[a-zA-Z\s]*$', message="Only letter is allowed!")], 
                required=True, widget=forms.TextInput(attrs={'placeholder':'Title', 'style':'font-size: 13px; text-transform: capitalize'}))
    
    posted_by = forms.CharField(label="Post by", min_length=3, validators= [RegexValidator(r'^[a-zA-Z\s]*$', message="Only letter is allowed!")], 
                required=True, widget=forms.TextInput(attrs={'placeholder':'Posted by', 'style':'font-size: 13px; text-transform: capitalize'}))
    
    content = forms.CharField(label="Content", min_length=10, required=True, widget=CKEditorWidget())
    
    published_date = forms.DateField(label="Job Expiration Date", required=False, widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control datepicker-input'}))
    
    image = forms.FileField(label="Upload company logo", required=False, widget=forms.ClearableFileInput(attrs={'style':'font-size: 13px'}))
    
    url = forms.URLField(max_length=150, min_length=3, required=False, widget=forms.TextInput(attrs={'placeholder':'Enter the news link', 'style':'font-size: 13px;'}))
    
    class Meta:
        model = Release
        fields = ['title', 'posted_by', 'content', 'published_date', 'image', 'url']
        

class EventsForm(forms.ModelForm):
    title = forms.CharField(label="Title", min_length=3, validators= [RegexValidator(r'^[a-zA-Z\s]*$', message="Only letter is allowed!")], 
                required=True, widget=forms.TextInput(attrs={'placeholder':'Title', 'style':'font-size: 13px; text-transform: capitalize'}))
    
    posted_by = forms.CharField(label="Post by", min_length=3, validators= [RegexValidator(r'^[a-zA-Z\s]*$', message="Only letter is allowed!")], 
                required=True, widget=forms.TextInput(attrs={'placeholder':'Posted by', 'style':'font-size: 13px; text-transform: capitalize'}))
    
    content = forms.CharField(label="Content", min_length=10, required=True, widget=CKEditorWidget())
    
    published_date = forms.DateField(label="Job Expiration Date", required=False, widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control datepicker-input'}))
    
    image = forms.FileField(label="Upload company logo", required=False, widget=forms.ClearableFileInput(attrs={'style':'font-size: 13px'}))
    
    document = forms.FileField(label="Document", required=False, widget=forms.ClearableFileInput(attrs={'style':'font-size: 13px'}))
    
    class Meta:
        model = Release
        fields = ['title', 'posted_by', 'content', 'published_date', 'image', 'url']
        

class PodcastForm(forms.ModelForm):
    title = forms.CharField(label="Title", min_length=3, validators= [RegexValidator(r'^[a-zA-Z\s]*$', message="Only letter is allowed!")], 
                required=True, widget=forms.TextInput(attrs={'placeholder':'Title', 'style':'font-size: 13px; text-transform: capitalize'}))
    
    host = forms.CharField(label="Post by", min_length=3, validators= [RegexValidator(r'^[a-zA-Z\s]*$', message="Only letter is allowed!")], 
                required=True, widget=forms.TextInput(attrs={'placeholder':'Posted by', 'style':'font-size: 13px; text-transform: capitalize'}))
    
    description = forms.CharField(label="Content", min_length=10, required=True, widget=CKEditorWidget())
    
    published_date = forms.DateField(label="Job Expiration Date", required=False, widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control datepicker-input'}))
    
    image = forms.FileField(label="Upload company logo", required=False, widget=forms.ClearableFileInput(attrs={'style':'font-size: 13px'}))
    
    url = forms.URLField(max_length=150, min_length=3, required=False, widget=forms.TextInput(attrs={'placeholder':'Enter the podcast link', 'style':'font-size: 13px;'}))
    
    class Meta:
        model = Release
        fields = ['title', 'host', 'description', 'published_date', 'image', 'url']
        
        
class GalleryForm(forms.ModelForm):
    
    image = forms.FileField(label="Upload company logo", required=False, widget=forms.ClearableFileInput(attrs={'style':'font-size: 13px'}))
    
    class Meta:
        model = Release
        fields = ['image']
        
        
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