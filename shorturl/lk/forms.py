from django import forms

class Authform(forms.Form):
    username = forms.CharField(max_length= 25,label="Введите ваше имя")
    password = forms.CharField(max_length= 30, label='Password', widget=forms.PasswordInput)