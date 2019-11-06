from django import forms
from django.contrib.auth.models import User


class SignUpForm(forms.ModelForm):
    """
    Signup form
    """
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "email")

    def clean_email(self):
        """method to check email validation"""
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            return forms.ValidationError("This email address already registered!")
        return email

    def clean_password(self):
        """method to check password validation"""
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            return forms.ValidationError("Password doesn't match")
        return password2

    def save(self, commit=True):
        """overriding save method to set password"""
        user = super(SignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user













