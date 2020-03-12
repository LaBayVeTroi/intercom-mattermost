from django.urls import path
from .views import (
  hello_world,
  recieve_intercom_hook
)
from .mattermost_api import (
  create_user,
  login
)

urlpatterns = [
  path('/hello-world', hello_world, name='index'),
  path('recieve_intercom_hook/', recieve_intercom_hook, name='recieve_intercom_hook'),
  path('create_user/', create_user, name='create_user'),
  path('login/', login, name='login')
]