# HELP ME GOD.
from django.shortcuts import render
from django.http import JsonResponse
from .models import User

# import django drf api views
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer

from rest_framework_simplejwt.tokens import RefreshToken

# import django login
from django.contrib.auth import login, logout


@api_view(["POST"])
def registeruser(request):
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Generate tokens
            refresh = RefreshToken.for_user(user)

            response = {
                "status": "success",
                "message": "Registration successful",
                "data": {
                    "accessToken": str(refresh.access_token),
                    "user": serializer.data,
                },
            }

            return Response(response, status=status.HTTP_201_CREATED)
        else:
            # Handle serializer validation errors
            errors = []
            for field, messages in serializer.errors.items():
                for message in messages:
                    errors.append({"field": field, "message": message})

            return Response({"errors": errors}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "GET":
        return JsonResponse({"hello": "HELLO WORLD"}, safe=False)


from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(["POST"])
def loginuser(request):
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        email = request.data.get("email")
        password = request.data.get("password")

        # Check if email and password are provided
        if not email or not password:
            return Response(
                {
                    "status": "Bad request",
                    "message": "Please provide both email and password",
                    "statusCode": status.HTTP_400_BAD_REQUEST,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Authenticate user
        user = authenticate(email=email, password=password)

        # Check if user exists and credentials are correct
        if user is None:
            return Response(
                {
                    "status": "Bad request",
                    "message": "Invalid credentials",
                    "statusCode": status.HTTP_401_UNAUTHORIZED,
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )

        # because of jwt we are not going to login the user into a session.
        # Generate tokens
        refresh = RefreshToken.for_user(user)

        print('serializer', type(serializer))

        # check if user has phone number, if not don't return phone number as response
        



        response = {
            "status": "success",
            "message": "Login successful",
            "data": {
                "accessToken": str(refresh.access_token),
                "user": UserSerializer(user).data,
            },
        }

        return Response(response, status=status.HTTP_200_OK)
