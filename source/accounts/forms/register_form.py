from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError



class MyUserCreationForm(UserCreationForm):

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if not email:
            self.add_error('email', 'Введите свой email')
        if not first_name and not last_name:
            self.add_error('first_name', 'Введите имя или фамилию')
            self.add_error('last_name', 'Введите имя или фамилию')

        return cleaned_data

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']
        error_messages = {
            "email": {
                "required": "Поле обязательное"}
        }
