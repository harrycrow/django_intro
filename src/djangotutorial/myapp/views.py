from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from .forms import CustomLoginForm

class CustomLoginView(LoginView):
    template_name = 'myapp/login.html'
    authentication_form = CustomLoginForm

class ProfileView(TemplateView):
    template_name = 'myapp/profile.html'
