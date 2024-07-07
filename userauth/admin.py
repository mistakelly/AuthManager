from django.contrib import admin
from django.contrib.auth import get_user_model

# get the active user model.
User = get_user_model()


# Register User model
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Admin configuration for the User model.

    Attributes:
        search_fields (list): Fields that can be searched in the admin interface.
        list_display (list): Fields displayed as columns in the admin interface.

    Usage:
        This admin interface allows managing user accounts with fields like email,
        username, active status, and last login timestamp.

    """
    search_fields = ['email']
    list_display = ['email', 'firstName', 'lastName', 'is_active', 'last_login']