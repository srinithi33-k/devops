from django.urls import re_path
from .views import get_user_view,create_user_view


urlpatterns=[
    re_path(r"^alumniapi/get-user/?$",get_user_view,name="get_user"),
    re_path(r"^alumniapi/create-user/?$",create_user_view,name="create_user"),
    # re_path(r"^alumniapi/login-user/?$",login_user_view,name="login_user"),
    # re_path(r"^alumniapi/nomination-details/?$",nomination_view,name="nomination_view"),
    # re_path(r"^alumniapi/event-register/?$",event_register_details,name="event_register"),
]