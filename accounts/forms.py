from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MyUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        # model = get_user_model()
        model = MyUser
        # fields = '__all__'
        fields = ['nickname', 'email', 'password1', 'password2', 'gender', 'birth',]
        GENDER_CHOICE = (
            ('남', '남'), ('여', '여')
        )
        widgets = {
            'gender': forms.Select(choices=GENDER_CHOICE),
            'birth': forms.DateTimeInput(attrs={
                'class': 'form-control datetimepicker-input',
                'data-target': '#datetimepicker1'
            })
        }

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['nickname', 'email', 'password']