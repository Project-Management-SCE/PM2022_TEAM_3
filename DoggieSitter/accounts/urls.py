# accounts/urls.py
from django.urls import path
from django.views.generic import TemplateView
from . import views, admin
from .views import PasswordsChangeView
from .views import Terms, Add, Feedback, ShowFeedback
<<<<<<< Updated upstream
<<<<<<< Updated upstream
from dog.views import AddDog

=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes

urlpatterns = [
    path(" ", views.go_home, name="home"),
    path("signup/", views.SignUpView, name="signup"),
    path('about', TemplateView.as_view(template_name='about.html'), name='about'),
    path('gallery', TemplateView.as_view(template_name='gallery.html'), name='gallery'),
    path("user_info/", views.GetAccounts, name="user_info"),
    path('admin_actions/make_admin', admin.make_new_admin, name='admin_actions/make_admin'),
    path("admin_actions/remove_admin", admin.delete_admin, name="admin_actions/remove_admin"),
    path('admin_actions/delete_user', admin.delete_user, name='admin_actions/delete_user'),
    path('admin_actions/approve_doggiesitter', admin.approve_doggiesitter, name='admin_actions/approve_doggiesitter'),
    path('admin_actions/', views.SearchUserByID, name='admin_actions'),
    path('change/<user_id>', views.changeAccount.as_view(), name='changeinfo'),
    path('change_password/<un>', views.GetUsername, name='change_password'),
    path('change_password2/', views.ChangePassword, name='change_password2'),
    path('Terms', views.Terms, name="Terms"),
    path('Feedback', views.Feedback, name="Feedback"),
    path('ShowFeedback', ShowFeedback.as_view(), name="ShowFeedback"),
    path('Add', views.Add, name="Add"),
    path('vet_map/<un>', views.Vet_Map, name="vet_map"),
<<<<<<< Updated upstream
<<<<<<< Updated upstream
    path('parks/<un>', views.Parks, name="parks"),
    path('DogPage/<user_id>', views.DogPage.as_view(), name='DogPage'),
    path("addtrip/<usr>", views.AddTrip, name="addtrip"),
    path("alltrips/", views.AllTrips, name="alltrips"),
    path('dogs', views.dogs, name="dogs"),
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes

]
