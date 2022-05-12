# accounts/views.py
from time import sleep
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.views import View
from .forms import ExtendedUserCreationForm, AccountsProfileForm, AccountChangeForm, TermsForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import Accounts, PostTerms, PostFeedback
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
import googlemaps
from geopy.geocoders import Nominatim
from pprint import pprint
from django.views.generic import ListView, DetailView


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
        return render(request, 'change.html', {'form_user': form, 'ok?': 'yes!'})

    def post(self, request, user_id):
        form = AccountChangeForm(request.POST)
        if form.is_valid():
            user = User.objects.get(pk=user_id)
            account = Accounts.objects.get(user=user)
            account.first_name = form.cleaned_data['first_name']
            account.last_name = form.cleaned_data['last_name']
            account.email = form.cleaned_data['email']
            account.phone_number = form.cleaned_data['phone_number']
            account.save()
            return render(request, 'home.html', {'ok?': 'form is valid!'})
        return render(request, 'change.html', {'form_user': form, 'ok?': 'form is not valid!'})

def GetUsername(request, un):
    user = User.objects.get(username=un)
    return render(request, 'change_password.html', {'user': user})
def go_home(request,temp):
    return render(request,temp)
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
        return render(request, 'home.html',{'Term': 'Try Worked'})
    else:
        pt = PostTerms.objects.all()
        return render(request, 'Terms.html', {'pt': pt})


def Add(request):
    pt = PostTerms.objects.all()
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        profile_form = AccountsProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return render(request, 'home.html', {'add': 'done'})
        else:
            return render(request, 'registration/Add.html',
                          {'form': form, 'profile_form': profile_form, 'pt': pt,
                           'error': "Bad Data Please Try Again"})
    else:
        form = ExtendedUserCreationForm()
        profile_form = AccountsProfileForm()
    context = {'form': form, 'profile_form': profile_form, 'error': "Bad Data Please Try Again", 'pt': pt}
    return render(request, 'registration/Add.html', context)


def Vet_Map(request, un):
    API_KEY = "AIzaSyA1NSKaMXW4cC5k9RB8dtOqlfZq9v7FNHc"
    map_client = googlemaps.Client(API_KEY)
    app = Nominatim(user_agent="tutorial")

    location_name = "Veterinary Clinic, "
    location = ""

    for i in Accounts.objects.all():
        if str(i) == str(un):
            user = Accounts.objects.get(id=i.id)
            location_name += user.city
            location = app.geocode("Israel, " + str(user.city)).raw

    city = {'lat': location['lat'], 'lng': location['lon']}

    try:
        response = map_client.places(query=location_name)
        results = response.get('results')
    except Exception as e:
        print(e)
        return None

    # pprint(results)


    location_data = []
    for i in results:
        location_data.append(i['geometry']['location'])
        (location_data[location_data.index(i['geometry']['location'])])['name'] = i['name']

        try:
            if i['opening_hours'].values() == True:
                (location_data[location_data.index(i['geometry']['location'])])['opening_hours'] = "Open"
            else:
                (location_data[location_data.index(i['geometry']['location'])])['opening_hours'] = "Close"
        except:
            break

    return render(request, 'vet_map.html', {'location_data': location_data, 'city': city})

def Feedback(request):
    if request.method == 'POST':
        post = PostFeedback()
        post.body = request.POST.get("body_name")
        post.author = request.POST.get("author_name")
        post.about = request.POST.get("about_id")
        post.save()
        return render(request, 'home.html')
    else:
        pt = PostFeedback.objects.all()
        return render(request, 'Feedback.html', {'pt': pt})

class ShowFeedback(ListView):
    model = PostFeedback
    template_name =  'ShowFeedback.html'
