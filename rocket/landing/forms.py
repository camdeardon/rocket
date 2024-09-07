from django import forms
from .models import User

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'account_type', 'bio_interests', 'bio_background', 'bio_projects']
        widgets = {
            'password': forms.PasswordInput(),
        }

