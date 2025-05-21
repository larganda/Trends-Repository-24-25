from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, EBikeRegistration

class CustomUserCreationForm(UserCreationForm):
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2', 'role']

class CustomAuthenticationForm(AuthenticationForm):
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES, widget=forms.RadioSelect)

class EBikeRegistrationForm(forms.ModelForm):
    purchase_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = EBikeRegistration
        exclude = ['owner']
        fields = [
            'full_name', 'email', 'phone', 'address',
            'ebike_brand', 'ebike_model', 'ebike_color',
            'ebike_serial_number', 'purchase_date', 'notes'
        ]
