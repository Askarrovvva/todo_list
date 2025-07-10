from django import forms
from django.core.exceptions import ValidationError
from .models import Issue
from django.forms import widgets


class IssueForm(forms.ModelForm):
    def clean_summary(self):
        summary = self.cleaned_data['summary']
        if len(summary) <= 3:
            raise ValidationError("Описание слишком краткое. Пожалуйста, добавьте больше деталей, "
                                  "чтобы сделать его информативным ")
        else:
            return summary

    class Meta:
        model = Issue
        fields = ['description', 'summary', 'statuses', 'types']
        error_messages = {
            "summary": {
                "required": "Поле обязательное"},

        }
        widgets = {
            'description': widgets.Textarea(attrs={'cols': 20, "rows": 5}),
        }