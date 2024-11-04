from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser

class UserAdmin(BaseUserAdmin):
    # 리스트에 표시할 필드 지정
    list_display = ('email', 'username', 'phone_number', 'is_admin', 'is_active')

    search_fields = ('email', 'username', 'phone_number')

    list_filter = ('is_admin', 'is_active')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('username', 'phone_number')}),
        ('Permissions', {'fields': ('is_admin', 'is_active')}),
    )

    readonly_fields = ('is_admin',)
    ordering = ('email',)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'phone_number', 'password1', 'password2'),
        }),
    )

admin.site.register(CustomUser, UserAdmin)