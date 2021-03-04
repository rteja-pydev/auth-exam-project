from django import forms

class UserCreationForm(forms.Form):
    Username = forms.CharField()
    Password = forms.CharField(widget=forms.PasswordInput)
    # Password2 = forms.CharField(widget=forms.PasswordInput)
