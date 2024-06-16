from django import forms
from .models import Rent
class RentForm(forms.ModelForm):
        """Form definition for Rent."""
    
        class Meta:
            """Meta definition for Rentform."""
    
            model = Rent
            fields = '__all__'
           