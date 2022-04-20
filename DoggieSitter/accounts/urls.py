# accounts/urls.py
from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("signup/", views.SignUpView, name="signup"),
    path('about', TemplateView.as_view(template_name='about.html'), name='about'),
    path('gallery', TemplateView.as_view(template_name='gallery.html'), name='gallery'),
    path("user_info/", views.GetAccounts, name="user_info"),
    path('about', TemplateView.as_view(template_name='about.html'), name='contact'),
    path('Change', TemplateView.as_view(template_name='change.html'), name='change'),

]