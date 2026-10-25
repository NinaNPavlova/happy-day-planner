from django import forms
from .models import Gift

class GiftForm(forms.ModelForm):
    class Meta:
        model = Gift
        fields = ['gift', 'person']


        labels = {
           'gift': 'Gift',
           'person': 'Person'
        }
        widgets = {
            'gift': forms.TextInput(attrs={'placeholder': 'Please input the gift:'}),
        }

        error_messages = {
            'gift': {'required': 'Please enter the gift.'},

        }
        help_texts = {
            'gift': 'Please enter the gift you want to give.',

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['person'].disabled = True

