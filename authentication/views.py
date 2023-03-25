from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import *
from .models import CustomUser
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import logout




@api_view(['GET'])
def api_endpoints(request):
    endpoints = [
        {
            'Endpoint': '/register',
            'HTTP Method': 'POST',
            'description': 'Submit user details for account creation'
        },
        {
            'Endpoint': '/users/id',
            'HTTP Method': 'GET',
            'description': 'Get  registered Users by ID'
        },
        {
            'Endpoint': '/Users',
            'HTTP Method': 'GET',
            'description': 'Get all registered Users'
        },
      
  
    ]
    
    return Response(endpoints)




@api_view(['POST'])
def registration_view(request):
    
    if request.method =='POST':
        serializer = RegisterationSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "successfully registered a new user"
            data['email'] = account.email
            data['username'] = account.username
            data['department'] = account.department
            token = Token.objects.get(user = account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)
    
    


@api_view(["GET"])
def userId(request,pk):
    users = CustomUser.objects.get(id = pk)
    serializer = RegisterationSerializer(users, many = False)
    return JsonResponse(serializer.data, safe=False)
    
    
    
@api_view(["GET"])
def getUsers(request):
    users = CustomUser.objects.all()
    serializer = RegisterationSerializer(users, many = True)
    return JsonResponse(serializer.data, safe=False)
    
    
    
    
    
    
    
    
# @api_view(['POST'])
# def logout_view(request):
    
#     if request == 'POST':
#         request.user.auth_token.delete()
#         return Response(status=status.HTTP_200_OK)
    
    
    
