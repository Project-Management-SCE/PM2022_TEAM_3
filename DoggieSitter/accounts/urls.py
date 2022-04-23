# accounts/urls.py
from django.urls import path
from django.views.generic import TemplateView
from . import views
from django.contrib.auth import views as auth_views
from .views import PasswordsChangeView

urlpatterns = [
    path("signup/", views.SignUpView, name="signup"),
    path('about', TemplateView.as_view(template_name='about.html'), name='about'),
    path('gallery', TemplateView.as_view(template_name='gallery.html'), name='gallery'),
    path("user_info/", views.GetAccounts, name="user_info"),
    path('password/', PasswordsChangeView.as_view(template_name='change-password.html'), name="password"),
    path('password_success', views.password_success, name="password_success"),
]
