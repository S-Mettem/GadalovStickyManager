"""
Forms mainApp ManagerSticky
"""
from django import forms
from .models import Sticky


class StickyCreationForm(forms.ModelForm):
    class Meta:

        model = Sticky
        fields = ['title', 'content', 'category']
        labels = {'title': 'Title',
                  'content': 'Content', 'category': 'Category'}
