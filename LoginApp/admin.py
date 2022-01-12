from django.contrib import admin
from .models import UserModel
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import RegistrationForm

from django.contrib.auth.admin import UserAdmin


# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = UserModel
    add_form = RegistrationForm
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Other Personal info',
            {
                'fields': (
                    'mobile',
                )
            }
        )
    )


admin.site.register(UserModel, CustomUserAdmin)

#admin.site.register(UserModel )