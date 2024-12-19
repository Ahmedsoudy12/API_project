from django.urls import path
from .views import get_users, create_user, user_detail


urlpatterns = [
    path('users/',get_users,name="get_users"),    # This is the route that i use to make an API request
                                       # get_user is the function that we are calling when we are making the request
    path('users/create',create_user,name="create_user"),
    path('users/<int:pk>',user_detail,name="user_detail"),  # 34an a input el id bta3 el user elly 3ayz a3mello edit
]