from django.contrib.auth.admin import UserAdmin
from user.models import User
from django.contrib import admin


class MyUserAdmin(UserAdmin):
    model = User
    list_display = ('username','balance_usd', 'balance_rdw')  # Contain only fields in your `custom-user-model`

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('phone',
                        'balance_usd',
                        'balance_rdw',)}),
    )

admin.site.register(User, MyUserAdmin)