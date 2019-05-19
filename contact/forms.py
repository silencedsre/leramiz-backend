from django import forms

class Inquire(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Your Email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Your Message'}))