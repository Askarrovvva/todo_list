from django import forms
from django.core.exceptions import ValidationError
from webapp.models import Issue, Type, Status
from django.forms import widgets


class IssueForm(forms.ModelForm):
    statuses = forms.ModelChoiceField(queryset=Status.objects.all())
    types = forms.ModelMultipleChoiceField(queryset=Type.objects.all())

    def clean_summary(self):
        summary = self.cleaned_data['summary']
        if len(summary) <= 3:
            raise ValidationError("Введённое описание слишком короткое. Добавьте дополнительные детали.")
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