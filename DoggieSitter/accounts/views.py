# accounts/views.py
from django.contrib.auth.models import User

from .forms import ExtendedUserCreationForm, AccountsProfileForm, AccountChangeForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import Accounts
from django.views import View


def SignUpView(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        profile_form = AccountsProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("home")
        else:
            return render(request, 'registration/signup.html',
                          {'form': form, 'profile_form': profile_form, 'error': "Bad Data Please Try Again"})
    else:
        form = ExtendedUserCreationForm()
        profile_form = AccountsProfileForm()
    context = {'form': form, 'profile_form': profile_form, 'error': ""}
    return render(request, 'registration/signup.html', context)


def GetAccounts(request):
    acc = Accounts.objects.all()
    usr = User.objects.all()
    return render(request, 'user_info.html', {'acc': acc, 'usr': usr})


class changeAccount(View):

    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        account = Accounts.objects.get(user=user)
        form = AccountChangeForm(instance=account)
        return render(request, 'change.html', {'form_user': form})

    def post(self, request, user_id):
        form = AccountChangeForm(request.POST)
        if form.is_valid():
            user = User.objects.get(pk=user_id)
            account = Accounts.objects.get(user=user)
            account.first_name = form.cleaned_data['first_name']
            account.last_name = form.cleaned_data['last_name']
            account.email = form.cleaned_data['email']
            account.save()
            return render(request, 'home.html')
        return render(request, 'change.html', {'form_user': form})
