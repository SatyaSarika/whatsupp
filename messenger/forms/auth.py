from django import forms

class SignupDETAILS(forms.Form):
    first_name=forms.CharField(label="FirstName")
    last_name=forms.CharField(label="lastname")
    username=forms.CharField(label="UserName")
    password=forms.CharField(label="passwordName",widget=forms.PasswordInput())

class LoginupDETAILS(forms.Form):
    username=forms.CharField(label="username")
    password=forms.CharField(label="password",widget=forms.PasswordInput())


