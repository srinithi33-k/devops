from rest_framework.decorators import api_view
from myapp.source.modules.RegisterUser import RegisterUser
from myapp.source.modules.CreateUser import CreateUser
# from myapp.source.modules.UserProfile import UserProfile
# from myapp.source.modules.NominationDetails import NominationDetails
# from myapp.source.modules.EventRegister import EventRegister


@api_view(['post'])
def get_user_view(request):
    return RegisterUser.register_user(request)

@api_view(['post'])
def create_user_view(request):
    return CreateUser.create_user(request)

# @api_view(['post'])
# def login_user_view(request):
#     return UserProfile.user_profile(request)

# @api_view(['post']) 
# def  nomination_view(request):
#     return  NominationDetails.nomination_details(request)

# @api_view(['post'])
# def event_register_details(request):
#     return EventRegister.event_register(request)

