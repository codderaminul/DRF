from django.urls import path
from users.views import CustomUserCreate

app_name = 'users'

urlpatterns = [
    path('',CustomUserCreate.as_view(),name="create_user"),
    path('register/',CustomUserCreate.as_view(),name="create_user"),
]













