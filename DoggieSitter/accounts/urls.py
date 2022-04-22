# accounts/urls.py
from django.urls import path, reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from . import views
from .forms import MyPasswordChangeForm


urlpatterns = [
    path("signup/", views.SignUpView, name="signup"),
    path('about', TemplateView.as_view(template_name='about.html'), name='about'),
    path('gallery', TemplateView.as_view(template_name='gallery.html'), name='gallery'),
    path("user_info/", views.GetAccounts, name="user_info"),
    path('about', TemplateView.as_view(template_name='about.html'), name='contact'),
    path('change_password/',
        PasswordChangeView.as_view(
            template_name='change_password.html',
            success_url=reverse_lazy('password_change_done'),
            form_class = MyPasswordChangeForm
         ),
         name='password_change'),

    path('change_password/done/',
        PasswordChangeDoneView.as_view(
            template_name='password_change_done.html'
        ),
        name='password_change_done'),
]
