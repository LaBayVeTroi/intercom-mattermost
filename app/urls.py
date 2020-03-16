from django.urls import path
# from .views import (
#   hello_world
# )
# from .mattermost_api import (
#   create_user,
#   login,
#   add_user_to_team,
#   add_user_to_channel,
#   forward_message_to_mattermost,
#   get_post_detail,
#   get_user_detail
# )
from .intercom_hook import (
  recieve_intercom_hook
)

from .mattermost_hook import recieve_mattermost_hook

# from .intercom_api import reply_conversation

urlpatterns = [
  path('recieve_intercom_hook/', recieve_intercom_hook, name='recieve_intercom_hook'),
  path('recieve_mattermost_hook/', recieve_mattermost_hook, name='recieve_mattermost_hook'),
]