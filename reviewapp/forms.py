from django import forms
from .models import Reviews

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['name', 'email', 'age', 'gender','phone_number', 'review']
        labels = {
            'name': 'Full Name',
            'email': 'Email',
            'age': 'Age',
            'gender': 'Gender',
            'phone_number': 'Phone Number',
            'review': 'Your Review'
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'age': forms.NumberInput(attrs={'class':'form-control'}),
            'gender': forms.Select(attrs={'class':'form-control'}),
            'phone_number': forms.TextInput(attrs={'class':'form-control'}),
            'review': forms.Textarea(attrs={'class':'form-control'})
        }