from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, EBikeRegistration
from .forms import CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ['email', 'role', 'is_staff']
    ordering = ['email']
    fieldsets = (
        (None, {'fields': ('email', 'password', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'role', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(EBikeRegistration)
