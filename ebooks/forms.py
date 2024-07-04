from django import forms
from .models import EBook


class EBookForm(forms.ModelForm):
    class Meta:
        model = EBook
        fields = [
            'title',
            'author',
            'description',
            'price',
            'cover_image',
            'file',
            'category'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input-text'}),
            'author': forms.TextInput(attrs={'class': 'input-text'}),
            'description': forms.Textarea(attrs={'class': 'textarea'}),
            'price': forms.NumberInput(attrs={'class': 'input-text'}),
            'cover_image': forms.ClearableFileInput(
                attrs={'class': 'file-input'}
            ),
            'file': forms.ClearableFileInput(attrs={'class': 'file-input'}),
            'category': forms.Select(attrs={'class': 'select-input'}),
        }
