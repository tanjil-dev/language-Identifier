from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import CustomUser, Contact  # Import your custom user model
from allauth.account.models import EmailAddress  # Import EmailAddress model

# Unregister social accounts from the admin (since you don't need them)
from allauth.socialaccount.models import SocialAccount, SocialApp, SocialToken
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)
admin.site.unregister(SocialToken)

# Unregister EmailAddress model from admin
admin.site.unregister(EmailAddress)

# Unregister Group model first to avoid AlreadyRegistered error
admin.site.unregister(Group)

# Custom admin class to manage users
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'username', 'is_staff', 'is_active', 'date_joined')  # Customize the fields to display
    list_filter = ('is_staff', 'is_active', 'date_joined')  # Add filters for the admin
    search_fields = ('email', 'username')  # Allow search by email or username
    ordering = ('date_joined',)  # Order users by their join date

    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )

# Re-register the Group model to bring it back to the admin
admin.site.register(Group)
admin.site.register(Contact)

# Register the CustomUser model with the admin interface
admin.site.register(CustomUser, CustomUserAdmin)

class CustomAdminSite(admin.AdminSite):
    site_header = "My Custom Admin Header"  # Header text
    site_title = "My Admin"  # Title in the browser tab
    index_title = "Welcome to My Admin"  # Text on the admin dashboard page

# Instantiate your custom admin site
custom_admin_site = CustomAdminSite(name='custom_admin')