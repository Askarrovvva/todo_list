from django.contrib.auth import get_user_model, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView

from accounts.forms import MyUserCreationForm

User = get_user_model()

class RegistrationView(CreateView):
    template_name = 'accounts/registration.html'
    model = User
    form_class = MyUserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('webapp:main')
        return next_url