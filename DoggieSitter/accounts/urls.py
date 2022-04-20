# accounts/urls.py
from django.urls import path, include
from django.views.generic import TemplateView
from . import views,templates

urlpatterns = [
    path("signup/", views.SignUpView, name="signup"),
    path('about', TemplateView.as_view(template_name='about.html'), name='about'),
    path('gallery', TemplateView.as_view(template_name='gallery.html'), name='gallery'),
    path('about', TemplateView.as_view(template_name='about.html'), name='contact'),
]
