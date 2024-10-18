# from alumni_apis.source.common.query_constants import FETCH_LOGIN_USERS
# from alumni_apis.source.common.common_utils import cursor_creater
# from base64 import b64decode
# from alumni_apis.source.common.constants import GOOD_JSON,ERROR_JSON
# from jwt import encode
# from json import loads
# from django.http import JsonResponse

# class UserProfile:
#     @staticmethod
#     def user_profile(request):
#         try:
#             # sample_dict={"reg_no":"41111492","password":"SriSathish@93"}
#             sample_dict=loads(request.body)
#             field=(sample_dict.get("reg_no"),)
#             select_query = FETCH_LOGIN_USERS % field
#             # print(select_query)
#             connect,cursor=cursor_creater()
#             cursor.execute(select_query)
#             if cursor.rowcount == 1:
#                 record=cursor.fetchone()[0][0]
#                 decoded_crtpassword = b64decode(record.get("password")).decode()
#                 if decoded_crtpassword==sample_dict.get("password"):
#                     token=encode(sample_dict,'uoqdoolW0ZPOBI_qGNjpXnlpAPW3iNi3rS3_9NL36xo',algorithm='HS256')
#                     GOOD_JSON["token"]=token
#                     print(GOOD_JSON)
#                     return JsonResponse(GOOD_JSON,status=200)
#                 else:
#                     raise Exception("Invalid reg_no or password!")   
        
#             else:
#                 raise Exception("user does not exist! try to signup")        
#         except Exception as error:
#             ERROR_JSON["reason"]=str(error)
#             return JsonResponse (ERROR_JSON,status=400)       



