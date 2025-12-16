from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

# ==============================
# REGISTER FORM
# ==============================
class CustomUserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# ==============================
# EDIT USER BASIC FORM
# ==============================
class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': 'required'}),
        }


# ==============================
# COUNTRY CODE OPTIONS
# ==============================
COUNTRY_CODES = [
    ("+91", "🇮🇳 +91"),
    ("+1", "🇺🇸 +1"),
    ("+44", "🇬🇧 +44"),
    ("+61", "🇦🇺 +61"),
    ("+971", "🇦🇪 +971"),
]


# ==============================
# EDIT PROFILE FORM
# ==============================
class EditProfileForm(forms.ModelForm):

    country_code = forms.ChoiceField(
        choices=COUNTRY_CODES,
        required=True
    )

    profile_pic = forms.ImageField(
        required=True
    )

    class Meta:
        model = Profile
        fields = ["profile_pic", "profession", "bio", "country_code", "phone", "address"]

        widgets = {
            "bio": forms.Textarea(attrs={
                "rows": 3,
                "class": "form-control",
                "required": "required",
            }),
            "profession": forms.TextInput(attrs={
                "class": "form-control",
                "required": "required",
            }),
            "profile_pic": forms.ClearableFileInput(attrs={
                "class": "form-control",
                "required": "required",
            }),
            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "required": "required",
            }),
            "address": forms.TextInput(attrs={
                "class": "form-control",
                "required": "required",
            }),
        }
