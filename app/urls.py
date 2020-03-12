from django.urls import path
from .views import (
  hello_world
)
from .mattermost_api import (
  create_user,
  login,
  add_user_to_team,
  add_user_to_channel,
  forward_message_to_mattermost
)
from .intercom_hook import (
  recieve_intercom_hook
)

urlpatterns = [
  path('hello-world/', hello_world, name='index'),
  path('recieve_intercom_hook/', recieve_intercom_hook, name='recieve_intercom_hook'),
  path('create_user/', create_user, name='create_user'),
  path('login/', login, name='login'),
  path('add_user_to_team/', add_user_to_team, name='add_user_to_team'),
  path('forward_message_to_mattermost/', forward_message_to_mattermost, name='forward_message_to_mattermost'),
  path('add_user_to_channel/', add_user_to_channel, name='add_user_to_channel'),
  # path('get_message_detail_from_mattermost/', get_message_detail_from_mattermost, name='get_message_detail_from_mattermost'),
]