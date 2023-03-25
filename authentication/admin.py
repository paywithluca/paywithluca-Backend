from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *



class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = ['pk', 'email', 'username', 'first_name', 'last_name', 'department']
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields':('email', 'first_name', 'last_name', 
         'department',)}),
    )

    # fieldsets = UserAdmin.fieldsets + (
    #     (None, {'fields': ('display_name','department',)}),
    #     )

admin.site.register(CustomUser, CustomUserAdmin)


