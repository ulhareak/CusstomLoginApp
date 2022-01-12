from django import forms
from django.forms.fields import CharField
from django.forms.widgets import PasswordInput
from .models import UserModel


class LoginForm(forms.Form):
    userid = forms.CharField(max_length=20)
    password = forms.CharField(max_length=30 , widget=PasswordInput())


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=PasswordInput())
    confirm_password = forms.CharField(
        widget=PasswordInput(), label='confirm password')

    class Meta:
        model = UserModel
        fields = [
            'username',
            'first_name', 'last_name',
            'email', 'mobile',
            'password', 'confirm_password'
        ]

    def clean(self, *args, **kwargs):
        cd = self.cleaned_data  # cleaned Data
        fields = [
            'username',
            'first_name', 'last_name',
            'email', 'mobile',
        ]

        print("avdhut ", type(cd))

        if cd['password'] != cd['confirm_password']:
            raise forms.ValidationError("Password Mis-Match")
        if cd['username'] in UserModel.objects.filter(username=cd['username']):
            raise forms.ValidationError('username exist')
        if cd['email'] in UserModel.objects.filter(email=cd['email']):
            raise forms.ValidationError('username exist')
        if cd['mobile'] in UserModel.objects.filter(mobile=cd['mobile']):
            raise forms.ValidationError('username exist')

        return super(RegistrationForm, self).clean(*args, **kwargs)


"""        for f in fields:
            value = cd[f]
            Q_set = UserModel.objects.filter(f = value)
            if value in Q_set:
                raise forms.ValidationError(value+" is already Exist")
"""


class ForgetpasswordForm(forms.Form):
    email = forms.EmailField(label="Enter email : ")
