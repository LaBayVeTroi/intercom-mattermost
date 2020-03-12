from django.urls import path
from .views import (
  ping_intercom
)

urlpatterns = [
  path('ping_intercom/', ping_intercom, name='ping_intercom')
]