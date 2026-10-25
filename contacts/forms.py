from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'surname', 'phone', 'year_of_birth', 'celebrations']

        labels = {
            'name': 'Name',
            'surname': 'Surname',
            'year_of_birth': 'Year of birth',
            'celebrations': 'Celebrations',
            'phone': 'Phone',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Please input the name:'}),
            'surname': forms.TextInput(attrs={'placeholder': 'Please input the surname:'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Please input the phone number:'}),
            'year_of_birth': forms.TextInput(attrs={'placeholder': 'Please input the year of birth:'}),
            'celebrations': forms.CheckboxSelectMultiple(),
        }

        error_messages = {
            'name': {'required': 'Please enter the name.'},
            'surname': {'required': 'Please enter the surname.'},
            'phone': {'required': 'Please enter the phone number.'},
            'year_of_birth': {'required': 'Please enter the year of birth.'},
        }
        help_texts = {
            'name': 'Please enter the name of your friend/family member.',
            'surname': 'Please enter the surname of your friend/family member.',
            'year_of_birth': 'Please enter the year of birth of your friend/family member.',
            'phone': 'Please enter the phone number of your friend/family member.',
        }
