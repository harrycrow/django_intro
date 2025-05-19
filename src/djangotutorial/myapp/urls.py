from django.urls import path
from .views import CustomLoginView, ProfileView


urlpatterns = [
    path('', CustomLoginView.as_view(), name='custom-login'),
    path('accounts/profile/', ProfileView.as_view(), name='profile'),
]