from django import forms
from django.core.exceptions import ValidationError
from webapp.models import Project
from django.forms import widgets


class ProjectForm(forms.ModelForm):

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) <= 3:
            raise ValidationError("Веденное описание слишком короткое. Добавьте дополнительные детали.")
        else:
            return title

    def clean_description(self):
        description = self.cleaned_data['description']
        if not len(description) <= 75:
            raise ValidationError("Это поле очень длинное, нужно меньше символов")
        else:
            return description

    class Meta:
        model = Project
        fields = ['title', 'description', 'end_date', 'start_date']
        error_messages = {
            "title": {
                "required": "Поле обязательное"},
            "start_date": {
                "required": "Поле обязательное"},

        }
        widgets = {
            'description': widgets.Textarea(attrs={'cols': 20, "rows": 5}),

        }