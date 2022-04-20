from django.contrib import admin
from .models import Accounts
from django.contrib.auth.models import User


# admin.site.register(Accounts)


@admin.action(description='Grant admin permissions')
def make_new_admin(modeladmin, request, queryset):
    user = User.objects.get(username=list(queryset)[0])
    user.is_superuser = True
    user.is_staff = True
    user.save()

@admin.action(description='Disable admin permissions')
def delete_admin(modeladmin, request, queryset):
    user = User.objects.get(username=list(queryset)[0])
    user.is_superuser = False
    user.is_staff = False
    user.save()

class NewAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'is_doggiesitter', 'approved']
    ordering = ['first_name', 'last_name']
    actions = [make_new_admin, delete_admin]


admin.site.register(Accounts, NewAdmin)

