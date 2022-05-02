# accounts/views.py
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.views import View
from .forms import ExtendedUserCreationForm, AccountsProfileForm, AccountChangeForm, TermsForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import Accounts, PostTerms
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'password_success.html', {})

def SignUpView(request):
    pt = PostTerms.objects.all()
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
                              {'form': form, 'profile_form': profile_form, 'pt': pt, 'error': "Bad Data Please Try Again"})
    else:
        form = ExtendedUserCreationForm()
        profile_form = AccountsProfileForm()
    context = {'form': form, 'profile_form': profile_form, 'error': "Bad Data Please Try Again", 'pt': pt}
    return render(request, 'registration/signup.html', context)

def GetAccounts(request):
    acc = Accounts.objects.all()
    usr = User.objects.all()
    return render(request, 'user_info.html', {'acc': acc, 'usr': usr})

def SearchUserByID(request):
    if request.method == 'POST':
        us = Accounts.objects.filter(id=request.POST.get("search_id"))
        if(len(us) == 0):
            return render(request, 'search_result.html', {'us': 'empty'})
        return render(request, 'search_result.html', {'us': us})
    return render(request, 'admin_actions.html')


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

def GetUsername(request, un):
    user = User.objects.get(username=un)
    return render(request, 'change_password.html', {'user': user})
def go_home(request,name):
    return render(request,name)

def ChangePassword(request):

    user = User.objects.get(username=request.POST.get("user_n"))
    if request.POST.get("new_pass1") == request.POST.get("new_pass2"):
        try:
            validate_password(request.POST.get("new_pass1"), user=user, password_validators=None)
            user.set_password(request.POST.get("new_pass1"))
            user.save()
            return render(request, 'pass_change_done.html', {'result_pass': "Password successfully changed."})
        except ValidationError as error:
            return render(request, 'change_password.html', {'error': error})
    else:
        return render(request, 'pass_change_done.html', {'result_pass': "The 2 passwords doesn't match."})


def Terms(request):
    term_form = TermsForm(request.POST)

    if request.method == 'POST' and not term_form.is_valid():
        try:
            post = PostTerms.objects.get(title=request.POST.get("title_name"))
        except:
            post = PostTerms()
            post.body = request.POST.get("body_name")
            post.author = request.POST.get("author_name")
            post.title = request.POST.get("title_name")
            post.save()
            return render(request, 'home.html')

        post.body = request.POST.get("body_name")
        post.author = request.POST.get("author_name")
        post.save()
        return render(request, 'home.html')
    else:
        pt = PostTerms.objects.all()
        return render(request, 'Terms.html', {'pt': pt})




