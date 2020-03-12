from django.shortcuts import render
from django.http import HttpResponse
from django.core.cache import cache
import redis
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

# Create your views here.

TTL = 60 * 120
MATTER_MOST_URL = 'https://mattermost-namnlnh.herokuapp.com/api/v4/'


def hello_world(request):
  d = {
    'id': '5e675ad457327e2c702451b0'
  }
  print(cache.set('5e675ad457327e2c702451b0', d, timeout=7200))
  print(cache.get('5e675ad457327e2c702451b0'))
  return HttpResponse('Hello World')