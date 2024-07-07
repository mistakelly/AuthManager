from django.contrib.auth.models import BaseUserManager
from uuid import uuid4


class CustomUserManager(BaseUserManager):
    """
    Custom manager for the User model.

    This manager provides methods to create both regular users and superusers.

    Methods:
        - create_user(email, password, **extrafields): Creates a regular user.
        - create_superuser(email, password, **extrafields): Creates a superuser with all permissions.

    Usage:
        Use this manager to create and manage user accounts with custom attributes.

    Example:
        manager = CustomUserManager()
        user = manager.create_user('user@example.com', 'password123')
        superuser = manager.create_superuser('admin@example.com', 'adminpassword')

    """

    def create_user(self, email, password=None, **extrafields):
        """
        Creates a regular user.

        Args:
            email (str): Email address of the user.
            password (str): Password for the user.
            **extrafields: Additional fields to be saved in the user model.

        Returns:
            User: Created user object.

        Raises:
            ValueError: If email is not provided.

        """
        if not email:
            raise ValueError("User email cannot be empty!!")

        # Normalize email address
        email = self.normalize_email(email)

        # Create user instance
        user = self.model(email=email, **extrafields)

        user.set_password(password)

        # Save user to the database
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extrafields):
        """
        Creates a superuser with all privileges and permissions.

        Args:
            email (str): Email address of the superuser.
            password (str): Password for the superuser.
            **extrafields: Additional fields to be saved in the superuser model.

        Returns:
            User: Created superuser object.

        Raises:
            ValueError: If is_staff or is_superuser flags are not set to True.

        """
        # Ensure superuser permissions are set
        extrafields.setdefault("is_staff", True)
        extrafields.setdefault("is_superuser", True)
        extrafields.setdefault("is_active", True)

        if extrafields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")

        if extrafields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")

        # Create the superuser
        return self.create_user(email, password, **extrafields)
