from django.urls import path
from .views import get_users, create_user


urlpatterns = [
    path('users/',get_users,name="get_users"),    # This is the route that i use to make an API request
                                       # get_user is the function that we are calling when we are making the request
    path('users/create',create_user,name="create_user"),
]