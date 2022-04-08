from django.forms import ModelForm
from .models import CustomUser


class UserForm(ModelForm):
    class Meta:
        model = CustomUser
        exclude = ('created_at', 'updated_at', 'last_login', 'password')
