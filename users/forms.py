from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserChangeForm,
    UserCreationForm,
)

from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Input your login"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Input your password"})
    )

    class Meta:
        model = User
        fields = ("username", "password")

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field_value in self.fields.items():
            field_value.widget.attrs["class"] = "form-control py-4"


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Input name"})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Input last name"})
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Input username"})
    )
    email = forms.CharField(
        widget=forms.EmailInput(attrs={"placeholder": "Input email"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Input password"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm password"})
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for field_name, field_value in self.fields.items():
            field_value.widget.attrs["class"] = "form-control py-4"


class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"readonly": True}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"readonly": True}))
    image = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "image")

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field_name, field_value in self.fields.items():
            field_value.widget.attrs["class"] = "form-control py-4"
        self.fields["image"].widget.attrs["class"] = "custom-file-input"
