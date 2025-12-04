from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User, Role

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Логин пользователя",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={'clacc':'form-control'})
    )

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])

        # Назначаем роль CUSTOMER
        role = Role.objects.get(name="CUSTOMER")
        user.role = role

        if commit:
            user.save()
        return user
