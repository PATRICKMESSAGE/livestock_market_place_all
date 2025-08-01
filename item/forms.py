from django import forms

from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ( 'category', 'name', 'description', 'price', 'image')
        
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'placeholder': 'Item name',
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Item description',
                'class': INPUT_CLASSES
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': 'Price in USD',
                'class': INPUT_CLASSES
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': INPUT_CLASSES
            })
        }
        
class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ( 'name', 'description', 'price', 'image', 'is_sold')
        
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Item name',
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Item description',
                'class': INPUT_CLASSES
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': 'Price in USD',
                'class': INPUT_CLASSES
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': INPUT_CLASSES
            })
        }