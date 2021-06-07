from django import forms
from django.contrib.auth.forms import UserCreationForm


class AuthForm(forms.Form):
    username = forms.CharField(max_length= 25,label="Введите ваше имя")
    password = forms.CharField(max_length= 30, label='Password', widget=forms.PasswordInput)


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user
