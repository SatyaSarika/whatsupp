from django.urls import path
from messenger.view import *

app_name="messenger"

urlpatterns = [
    path('signup/',SignupView.as_view(),name="sign_up"),
    path('login/',LoginView.as_view(),name="loginpage"),
    path('logout/',logout_user,name="logoutpage"),

    path('msg/',message_view.as_view(),name='msg'),
    path('msg/chat/<int:pk>',chat_view.as_view(),name='chat'),
]