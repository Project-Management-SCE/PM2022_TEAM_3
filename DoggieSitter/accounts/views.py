# accounts/views.py
from django.contrib.auth.models import User

from .forms import ExtendedUserCreationForm, AccountsProfileForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import Accounts


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
    # for i in acc:
    #     print(i.last_name)
    return render(request, 'user_info.html', {'acc': acc, 'usr': usr})