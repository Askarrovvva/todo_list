from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class UserForm(forms.Form):
    users = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
