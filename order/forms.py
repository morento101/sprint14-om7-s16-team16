from django.forms import ModelForm, TextInput
from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        exclude = ('created_at',)
        widgets = {
            'end_at': TextInput(attrs={'type': 'date'}),
            'plated_end_at': TextInput(attrs={'type': 'date'})
        }
