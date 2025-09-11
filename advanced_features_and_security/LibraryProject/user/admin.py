from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin


# Register your models here.

class ModelAdmin(UserAdmin):
    # Fields to display in the list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_of_birth')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    
    # Fields to show in the edit form, grouped by section
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Fields to show in the create form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)

admin.site.register(CustomUser, ModelAdmin)

