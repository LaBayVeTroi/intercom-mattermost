from django.urls import path
from .views import (
  hello_world,
  recieve_intercom_hook
)

urlpatterns = [
  path('/hello-world', hello_world, name='index'),
  path('recieve_intercom_hook/', recieve_intercom_hook, name='recieve_intercom_hook')
]