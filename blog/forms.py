from django import forms

class Comments(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Your Name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Your Email"}))
    comment = forms.CharField(widget=forms.Textarea(attrs={"placeholder":"Comments"}))