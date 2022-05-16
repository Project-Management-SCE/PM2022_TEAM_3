from datetime import date
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from django.core.validators import EmailValidator
from django.forms import SelectDateWidget
from .models import Accounts, PostTerms


class ExtendedUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user

class AccountsProfileForm(forms.ModelForm):

    class Meta:
        model = Accounts
        fields = ('first_name', 'last_name', 'gender', 'date_of_birth', 'id', 'email', 'phone_number', 'city', 'neighborhood', 'street', 'Aprt',  'is_doggiesitter')
        widgets = {
            'date_of_birth': SelectDateWidget(years=range(1902, date.today().year + 1)),
        }

    def clean_id(self):
        id = self.cleaned_data['id']
        if not id.isdigit():
            raise forms.ValidationError("ID must contain numbers only")
        if len(id) != 9:
            raise forms.ValidationError("ID number must be exactly 9 digits long")
        return id
    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if not phone_number.isdigit():
            raise forms.ValidationError("Phone number must contain numbers only")
        if len(phone_number) != 10:
            raise forms.ValidationError("Phone number must be exactly 10 digits long")
        return phone_number
    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']
        today = date.today()
        age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
        if age < 18:
            raise forms.ValidationError("Sorry, you have to be at least 18 years old in order to use our site's services.")
        if age > 120:
            raise forms.ValidationError("Sorry, you have to be at most 120 years old.")
        return date_of_birth
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not first_name.isalpha():
            raise forms.ValidationError("First name must contain letters only")
        return first_name
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if not last_name.isalpha():
            raise forms.ValidationError("Last name must contain letters only")
        return last_name
    def clean_email(self):
        email = self.cleaned_data['email']
        validator = EmailValidator()
        validator(email)
        return email


class AccountChangeForm(forms.ModelForm):
    class Meta:
        model = Accounts
        fields = ('first_name', 'last_name', 'email', 'phone_number')

    def clean_email(self):
        email = self.cleaned_data['email']
        validator = EmailValidator()
        validator(email)
        return email



class TermsForm(forms.ModelForm):
    class Meta():
        model = PostTerms
        fields = ('author', 'title', 'body')

    def clean_author(self):
        author = self.cleaned_data['author']
        for i in User.objects.all():
            if author == i.username and not i.is_superuser:
                print("Only admins can post here.")
                raise forms.ValidationError("Only admins can post here.")
        return author
    def clean_title(self):
        title = self.cleaned_data['title']
        if not title.isdigit():
            print("Title must be numeric")
            raise forms.ValidationError("Title must be numeric")
        if title <= 0:
            print("Title number must be greater than 1.")
            raise forms.ValidationError("Title number must be greater than 1.")
        return title
    def clean_body(self):
        body = self.cleaned_data['body']
        return body
