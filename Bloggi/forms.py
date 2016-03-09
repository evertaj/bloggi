from django import forms

class CommentForm(forms.Form):
    text = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':3, 'cols':87}))
