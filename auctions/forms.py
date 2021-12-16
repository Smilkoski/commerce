from django import forms

from .models import (
    Bid,
)


class BidForm(forms.ModelForm):
    price = forms.IntegerField()

    class Meta:
        model = Bid
        fields = ['price']
