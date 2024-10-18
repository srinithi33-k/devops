from psycopg2 import connect 
""" 
    #@Python Programs
    #@Name : DBInit.py
    #@Since : 23-01-2024
    #@Author : Srinithi K
    #@Version : 1.0
    #@See : This file is to done database related works."""

class DbInit():
    def __init__(self,data_base,database_username,password,port_no=5432,host="localhost"):
        self.database=data_base
        self.db_username=database_username
        self.password=password
        self.port_no=port_no
        self.host=host
    def db_connector(self):
        """Title : db_connector
           Args : db object
           Returns : This function is to connect db 
                     with the creted object attributes"""
        try:
            connector=connect(database=self.database,user=self.db_username,password=self.password,host=self.host,port=self.port_no)
            return connector
        except Exception as error:
            raise Exception(error)
                