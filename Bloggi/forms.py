from django import forms

class CommentForm(forms.Form):
    text = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':3, 'cols':40}))

class ArticleForm(forms.Form):
    title = forms.CharField(label='Title', widget=forms.Textarea(attrs={'rows':1, 'cols':140}))
    text = forms.CharField(label='Text', widget=forms.Textarea(attrs={'rows':3, 'cols':140}))
