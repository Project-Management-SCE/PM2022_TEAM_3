# accounts/urls.py
from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("signup/", views.SignUpView, name="signup"),
    path('about', TemplateView.as_view(template_name='about.html'), name='about'),
    path('gallery', TemplateView.as_view(template_name='gallery.html'), name='gallery'),
    path('user_info', TemplateView.as_view(template_name='user_info.html'), name='user_info'),
]