# import django rest framework serializers
from rest_framework import serializers

# # import the user model
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.

    This serializer provides a mapping between the User model and its JSON representation.

    Usage:
        Use this serializer to serialize and deserialize user objects to/from JSON.
    """

    class Meta:
        model = User
        fields = ["userId", "firstName", "lastName", "email", "password", "phone"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        """
        Create a new user instance.

        Args:
            validated_data (dict): Dictionary containing user data.

        Returns:
            User: Created user object.

        """

        return User.objects.create_user(**validated_data)
