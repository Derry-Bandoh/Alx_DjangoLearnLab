from django.contrib import admin
from .models import Book
from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Custom admin configuration for the Book model
class BookAdmin(admin.ModelAdmin):
    # Display these fields in the admin list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters in the right sidebar
    list_filter = ('author', 'publication_year')
    
    # Add search functionality
    search_fields = ('title', 'author')
    
    # Optional: Add ordering
    ordering = ('title',)
    
    # Optional: Control how many items are shown per page
    list_per_page = 20

# Register the Book model with the custom admin configuration
admin.site.register(Book, BookAdmin)




# Register your models here.

class CustomUserAdmin(UserAdmin):
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

admin.site.register(CustomUser, CustomUserAdmin)
