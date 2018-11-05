from django import forms
from django.core.validators import RegexValidator

from weibo.models import User


class LoginForm(forms.Form):
    email_sign_in = forms.EmailField(required=True, error_messages={'required': u'Email cannot be null',
                                                                    'invalid': u'enter a valid email address.'}, )
    password_sign_in = forms.CharField(widget=forms.PasswordInput(), min_length=6, required=True, )

    def clean_email_sign_in(self):
        email = self.cleaned_data['email_sign_in']
        have_email = User.objects.filter(email=email).count()
        if have_email == 0:
            raise forms.ValidationError('email not found.')
        return email


class RegisterForm(forms.Form):
    email_sign_up = forms.EmailField(required=True, error_messages={'required': u'Email cannot be null',
                                                                    'invalid': u'enter a valid email address.'}, )

    username_sign_up = forms.CharField(required=True,
                                       validators=[
                                           RegexValidator(
                                               regex='^[a-z]*$',
                                               message='username has illegal characters.',
                                               code='invalid_username'
                                           ),
                                       ]
                                       )
    password_sign_up = forms.CharField(widget=forms.PasswordInput(), required=True)
    password_cfm_sign_up = forms.CharField(widget=forms.PasswordInput(), required=True)

    def clean_email_sign_up(self):
        email = self.cleaned_data['email_sign_up']
        have_email = User.objects.filter(email=email).count()
        if have_email:
            raise forms.ValidationError('email already taken.')
        return email

    def clean_username_sign_up(self):
        usrname = self.cleaned_data['username_sign_up']
        have_name = User.objects.filter(username=usrname).count()
        if have_name:
            raise forms.ValidationError('email already taken.')
        return usrname

    def clean_password_sign_up(self):
        password = self.cleaned_data['password_sign_up']
        if len(password) < 6:
            raise forms.ValidationError('password too short.')
        return password

    def clean(self):
        cleaned_data = self.cleaned_data
        password = cleaned_data['password_sign_up']
        password_cfm = cleaned_data['password_cfm_sign_up']
        if password != password_cfm:
            raise forms.ValidationError('password mismatch.')
        return cleaned_data