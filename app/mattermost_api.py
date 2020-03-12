import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.cache import cache

MATTER_MOST_URL = 'https://mattermost-namnlnh.herokuapp.com/api/v4'
PASSWORD_CREATE_USER = '123456'
TOKEN_ADMIN_MATTERMOST = '51sdzcjrojnudeymx9z7zoitbe'
TEAM_ID = 'soqngurrzp8pzx7gt1ojwymsrr'
SERVICE_CHANNEL_ID = '3gnypxcd5jynfrhpnisy6ysdko'


# Create user
def create_user(user_id):
  req_data = {
    'email': '{}@gmail.com'.format(user_id),
    'username': '{}'.format(user_id),
    'password': PASSWORD_CREATE_USER
  } 
  end_point = '/users'
  req_headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {}'.format(TOKEN_ADMIN_MATTERMOST)
  }
  req_url = '{}/{}'.format(MATTER_MOST_URL, end_point)
  res = requests.post(url=req_url, headers=req_headers, json=req_data)
  res_json = res.json()
  return res_json['id']

def login(id_logged_in):
  req_data = {
    'login_id': 'id_logged_in',
    'password': PASSWORD_CREATE_USER
  }
  end_point = 'users/login'
  req_url = '{}/{}'.format(MATTER_MOST_URL, end_point)
  res = requests.post(url=req_url, json=req_data)
  # print(cache.get(id_logged_in))
  return token_mattermost

def add_user_to_team(mattermost_id):
  end_point = 'teams/{}/members'.format(TEAM_ID)
  req_data = {
    'user_id': mattermost_id,
    'team_id': TEAM_ID
  }
  req_headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {}'.format(TOKEN_ADMIN_MATTERMOST)
  }
  req_url = '{}/{}'.format(MATTER_MOST_URL, end_point)
  res = requests.post(url=req_url,headers=req_headers,json=req_data)
  print(res.json())
  return Response({'data': '1'})

def add_user_to_channel(token,mattermost_id):
  end_point= 'channels/{}/members'.format(SERVICE_CHANNEL_ID)
  req_url = '{}/{}'.format(MATTER_MOST_URL,end_point)
  req_data = {
    'user_id' : mattermost_id
  }
  req_headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {}'.format(token)
  }
  res = requests.post(url=req_url,headers=req_headers,json=req_data)
  print(res.json())

def forward_message_to_mattermost(token,root_id,message):
  end_point = 'posts'
  req_url = '{}/{}'.format(MATTER_MOST_URL,end_point)
  req_headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {}'.format(token)
  }
  req_data = {
    'channel_id': SERVICE_CHANNEL_ID,
    'message' : message,
    'root_id' : root_id
  }
  res = requests.post(url=req_url,headers=req_headers,json=req_data)
  print(res.json())
  return res.json()

# def get_message_detail_from_mattermost(token,message_id):
#     end_point = 'posts/{}'.format(message_id)
#     req_url = '{}/{}'.format(MATTER_MOST_URL,end_point)
#     req_headers = {
#       'Content-Type': 'application/json',
#       'Authorization': 'Bearer {}'.format(token)
#     }
#     res = requests.get(url=req_url,headers=req_headers)
#     print(res.json())
#     return res.json()