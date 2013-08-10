# http://stackoverflow.com/q/1214453/595990

from django.contrib import admin
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class MyUserCreationForm(UserCreationForm):
    username = forms.RegexField(
        label='Username',
        max_length=15,
        regex=r'^[a-zA-Z0-9_-]+$',
        help_text = 'Required. 15 characters or fewer. Alphanumeric characters only (letters, digits, hyphens and underscores).',
        error_message = 'This value must contain only letters, numbers, hyphens and underscores.')

class MyUserChangeForm(UserChangeForm):
    username = forms.RegexField(
        label='Username',
        max_length=15,
        regex=r'^[a-zA-Z0-9_-]+$',
        help_text = 'Required. 15 characters or fewer. Alphanumeric characters only (letters, digits, hyphens and underscores).',
        error_message = 'This value must contain only letters, numbers, hyphens and underscores.')

class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm

admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
