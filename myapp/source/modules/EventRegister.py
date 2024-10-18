# from alumni_apis.source.common.query_constants import EVENT_REGISTER_DETAILS,insert_query_marker,FETCH_AUTHORIZED_USERS
# from alumni_apis.source.common.common_utils import cursor_creater
# from alumni_apis.source.common.constants import GOOD_JSON,ERROR_JSON
# from alumni_apis.source.common.common_utils import is_email
# from jwt import decode
# from django.http import JsonResponse
# from json import loads


# class EventRegister:
    
#     def event_register(request):
#         try:
#             # sample_dict={"first_name":"sri","middle_name":"nithi","last_name":"k","year_of_passing":2025,"contact_no":8220834963,"email_id":"srinithi33.k@gmail.com","contact_address":"vivekanandha street 18/1 karaikudi"}
#             sample_dict=loads(request.body)
#             sample_dict["contact_no"]=str(sample_dict.get("contact_no"))
#             sample_dict["year_of_passing"]=str(sample_dict.get("year_of_passing"))
#             if not is_email(sample_dict.get("email_id")):
#                 raise Exception ("invalid email id")
#             incoming_token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZWdfbm8iOiI0MTExMTQ5MiIsInBhc3N3b3JkIjoiU3JpU2F0aGlzaEA5MyJ9.te45qM6YJK2q0EDOMdCd9HXCpdUN178Gq1Bb2kd_eT8'
#             decoded_token = decode(incoming_token,'uoqdoolW0ZPOBI_qGNjpXnlpAPW3iNi3rS3_9NL36xo',algorithms=['HS256'])
#             incoming_reg_no= decoded_token.get("reg_no")
#             connect,cursor = cursor_creater()
#             field = (incoming_reg_no,)
#             select_query = FETCH_AUTHORIZED_USERS % field
#             print(select_query)
#             cursor.execute(select_query)
#             if cursor.rowcount == 1:    
#                 sample_dict={key:"'"+ value +"'" for key,value in sample_dict.items()}
#                 insert=insert_query_marker("event_register_details",sample_dict)
#                 connect,cursor=cursor_creater()
#                 cursor.execute(insert)
#                 connect.commit()
#                 if cursor.rowcount == 1:     
#                     print(GOOD_JSON)
#                     return JsonResponse(GOOD_JSON,status=200)
#             else:
#                 raise Exception("user not authorized")             
#         except Exception as error:
#             ERROR_JSON["reason"]=error
#             print(ERROR_JSON)
#             return JsonResponse(ERROR_JSON,status=400)            