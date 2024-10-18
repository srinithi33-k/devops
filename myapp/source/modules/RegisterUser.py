from myapp.source.common.common_utils import is_password,is_email
from psycopg2 import IntegrityError
from myapp.source.common.common_utils import cursor_creater
from myapp.source.common.constants import GOOD_JSON,ERROR_JSON
from base64 import b64encode
from myapp.source.common.query_constants import FETCH_AUTHORIZED_USERS,insert_query_marker
from json import loads
from django.http import JsonResponse




class RegisterUser:
    @staticmethod
    def register_user(request):
        try:
            # sample_dict={"email_id":"srinithi33.k@gmail.com","reg_no":41111492,"name" :"srinithi k","password":"SriSathish@93" }
            # sample_dict=request.body
            # if not is_email(sample_dict.get("email_id")):
            #     raise Exception("invalid email")
            # if not is_password(sample_dict.get("password")):
            #     raise Exception("invalid password")
            # encoded_password =b64encode(sample_dict.get("password").encode()).decode()
            # sample_dict["reg_no"]=str(sample_dict.get("reg_no"))
            # sample_dict["password"]=encoded_password
            connect,cursor = cursor_creater()
            # field = (sample_dict.get("reg_no"),)
            select_query = FETCH_AUTHORIZED_USERS
            cursor.execute(select_query)
            
            # if cursor.rowcount == 1:
            # sample_dict={key:"'"+ value +"'" for key,value in sample_dict.items()}
            # insert_query=insert_query_marker("user_profile",sample_dict)
            # cursor.execute(insert_query)
            # connect.commit()
            # print(GOOD_JSON)
            GOOD_JSON["data"]=cursor.fetchone()[0]
            return JsonResponse(GOOD_JSON,status=200)
            # else:
            #     raise Exception("user authorization for alumni not allowed! please contact university for more information.")   
        # except IntegrityError as error:
        #     error_message=str(error)
        #     if 'duplicate key value violates unique constraint' in error_message:
        #         ERROR_JSON["reason"]="user already exist!"
        #         return JsonResponse(ERROR_JSON,status=400)
        except Exception as error:
            ERROR_JSON["reason"]=str(error)
            print(ERROR_JSON)  
            return JsonResponse(ERROR_JSON,status=400)  
      
