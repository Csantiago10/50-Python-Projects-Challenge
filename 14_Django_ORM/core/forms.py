from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    # 1. Create a form class inherit from forms.ModelForm
    class Meta:
        # 2. Define the model
        model = Profile
        # 3. Define the fields
        fields = ['name', 'role', 'skills']
        # 4. Define the widgets
        # Styles with CSS (Booststrap or my CSS)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre'}),
            'role': forms.TextInput(attrs={'class': 'form-control'}),
            'skills': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }