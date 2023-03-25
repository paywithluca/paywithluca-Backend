from django.urls import path
from .views import *
# from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', api_endpoints, name = "endpoint"),
    path('users', getUsers, name = "getUsers"),
    path('users/<str:pk>', userId, name = "userId"),
    path('register', registration_view, name = "register"),
    # path('logout', logout_view, name = "logout"),
    #  path('login', obtain_auth_token, name = "login"),
    
]
