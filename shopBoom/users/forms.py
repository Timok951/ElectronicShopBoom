from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User, Role, UserPreference, UserCredenetials


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])

        role = Role.objects.get(rolename="CUSTOMER")
        user.role = role

        if commit:
            user.save()
        return user


class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = UserPreference
        fields = ("theme", "date_format", "page_size", "saved_filters")
        widgets = {
            "saved_filters": forms.Textarea(attrs={"rows": 3}),
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email",)


class UserCredentialsForm(forms.ModelForm):
    class Meta:
        model = UserCredenetials
        fields = ("humanname", "phonenumber")
