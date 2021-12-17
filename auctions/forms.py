from django import forms

from .models import (
    Bid,
    Comment,
)


class BidForm(forms.ModelForm):
    price = forms.IntegerField()

    class Meta:
        model = Bid
        fields = ['price']


class CommentForm(forms.ModelForm):
    comment = forms.Textarea()

    class Meta:
        model = Comment
        fields = ['comment']
