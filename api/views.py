from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer

# Create your views here.



@api_view(['GET'])   # Here i am defining the get_user to be a GET request with the decorator api_view
def get_users(request):    # End point function
    users = User.objects.all()
    serilizer = UserSerializer(users)
    return Response(UserSerializer({'name':"Ahmed",'age':25}).data)    # returning a Response object and inside it the serialized data




@api_view(['POST'])   # Here i am defining the create_user to be a POST request with the decorator api_view
def create_user(request):    #
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 




