from django import forms
from .models import Celebration

class CelebrationForm(forms.ModelForm):
    class Meta:
        model = Celebration
        fields = ['celebration_type', 'title', 'day_of_month', 'month']

        labels = {
            'celebration_type': 'Type',
            'title': 'Title',
            'day_of_month': 'Day',
            'month': 'Month',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Please input the title of celebration'}),
        }
        error_messages = {
            'day_of_month': {'required': 'Please enter the day of the month.'},
            'month': {'required': 'Please enter the month.'},
        }
        help_texts = {
            'day_of_month': 'Please enter the number between 1 and 31.',
            'month': 'Please enter the number between 1 and 12.',
            'title': 'Required when the type is Other.',
        }
