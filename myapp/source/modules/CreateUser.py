from myapp.source.common.query_constants import insert_query_marker
from myapp.source.common.common_utils import cursor_creater
from myapp.source.common.constants import GOOD_JSON,ERROR_JSON
# from myapp.source.common.common_utils import is_email
from jwt import decode
from django.http import JsonResponse   


from json import loads

class CreateUser:
    def create_user(request):
        try:
            sample_dict=loads(request.body)
            sample_dict={key:"'"+ value +"'" for key,value in sample_dict.items()}
            insert=insert_query_marker("authorized_users",sample_dict)
            connect,cursor=cursor_creater()
            cursor.execute(insert)
            connect.commit()
            if cursor.rowcount == 1:     
                print(GOOD_JSON)
                return JsonResponse(GOOD_JSON,status=200)
            else:
                raise Exception("user not authorized")             
        except Exception as error:
            ERROR_JSON["reason"]=str(error)
            print(ERROR_JSON)
            return JsonResponse(ERROR_JSON,status=400)            