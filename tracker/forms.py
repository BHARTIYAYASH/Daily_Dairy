# from django import forms
# from .models import DailyConsumption

# class ConsumptionForm(forms.ModelForm):
#     class Meta:
#         model = DailyConsumption
#         fields = ['item', 'quantity']

from django import forms
from .models import DailyConsumption

class DailyConsumptionForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})  # Enables date selection
    )

    class Meta:
        model = DailyConsumption
        fields = ['date', 'item', 'quantity']
