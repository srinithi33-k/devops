
""" 
    #@Python Programs
    #@Name : constants.py
    #@Since : 14-01-2024
    #@Author : Srinithi K
    #@Version : 1.0
    #@See : This file contains the goodjson,errorjson msg"""


ALLOWABLE_AWARD_CATEGORY=["Best Entrepreneur","Rrsearcher","Exemplary Alumni Award(Best in dept/institution)","Best Social Worker","Best Industry Achiever"]
ALLOWABLE_AWARD_FIELD_WORKING=["IT","Goverment Sector","Enterpreneur","Others"]
success_msg = "Job Done, successflly"
fail_msg = "Some thing went wrong"
GOOD_JSON = {
    "status_code":200,
    "message":f"SUCCESS,{success_msg}"
}
ERROR_JSON = {
    "status_code":400,
    "message":f"FAILED,{fail_msg}"
}