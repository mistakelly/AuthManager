# api/views.py
from django.shortcuts import render

# Create your views here.
# api
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from userauth.models import User
from userauth.serializers import UserSerializer

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user(request, id):
    # Retrieve the user based on the provided id
    try:
        user = User.objects.get(userId=id)
    except User.DoesNotExist:
        return Response(
            {"status": "Not Found", "message": f"User with id {id} does not exist."},
            status=status.HTTP_404_NOT_FOUND,
        )

    # Check if the user requesting the data is either the user themselves or has access through an organization
    if user == request.user or user.organizations.filter(users=request.user).exists():
        serializer = UserSerializer(user)
        return Response(
            {
                "status": "success",
                "message": "User details retrieved successfully.",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )
    else:
        return Response(
            {
                "status": "Unauthorized",
                "message": "You are not authorized to access this user's details.",
            },
            status=status.HTTP_403_FORBIDDEN,
        )