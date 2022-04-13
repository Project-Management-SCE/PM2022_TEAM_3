# accounts/views.py

from .forms import ExtendedUserCreationForm, AccountsProfileForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
