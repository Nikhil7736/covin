from django.contrib import admin

# Register your models here.
from .models import booking


class signup(admin.ModelAdmin):
    list_display = ['first_name',
                    'last_name',
                    'username',
                    'Password',
                    'Repeat_Password',
                    'email', ]


admin.site.register(booking, signup)
