from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from datetime import date
from django.urls import reverse


class Accounts(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(validators=[MinLengthValidator(2)], max_length=50, blank=False)
    last_name = models.CharField(validators=[MinLengthValidator(2)], max_length=50, blank=False)
    email = models.CharField(validators=[MinLengthValidator(2)], max_length=50, blank=False)
    id = models.CharField(max_length=9,
                          validators=[MinLengthValidator(9)],
                          blank=False,
                          primary_key=True
    )
    gender = models.CharField(
        max_length=6,
        choices=[('male', 'male'), ('female', 'female')],
        blank=False,
    )
    date_of_birth = models.DateField(default=date.today)
    city = models.CharField(max_length=50,
                            blank=False,
    )
    neighborhood = models.CharField(max_length=50,
                                    blank=False,
    )
    street = models.CharField(max_length=50,
                              blank=False,
                              default="street and number"
    )
    Aprt = models.CharField(max_length=50,
                            blank=False,
                            default="Aprt. number"
    )
    phone_number = models.CharField(max_length=10,
                                    validators=[MinLengthValidator(10)],
                                    blank=False,
    )
    is_doggiesitter = models.BooleanField()
    is_admin = models.BooleanField(default=False, blank=True, null=True)
    approved = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.user.username

class PostTerms(models.Model):
    author = models.TextField()
    title = models.IntegerField()
    body = models.TextField()


    def __str__(self):
        return str(self.author) + '  |  terms'

    def get_absolute_url(self):
        return reverse('home')
