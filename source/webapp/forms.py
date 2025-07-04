from django import forms
from django.core.exceptions import ValidationError
from webapp.models import ToDo, status_choices
from django.forms import widgets

class ToDoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False
            field.widget.attrs['class'] = 'form-control'

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if not description:
            raise ValidationError("Поле обязательное")
        elif len(description) <= 3:
            raise ValidationError("Требуется написать минимум 3 символа")
        elif len(description) > 100:
            raise ValidationError("Описание не должно превышать 100 символов")
        return description

    def clean_description_detail(self):
        description_detail = self.cleaned_data.get('description_detail')
        if description_detail and len(description_detail) > 1000:
            raise ValidationError("Подробное описание не должно превышать 1000 символов")
        return description_detail

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    class Meta:
        model = ToDo
        fields = ['description', 'description_detail', 'status', 'date_completion']
        widgets = {
            "date_completion": widgets.DateInput(attrs={"type": "date"}),
        }
        error_messages = {
            "description": {"required": "Поле обязательное"}
        }