import psycopg2


class DbConnection:
    def __init__(self,hostname:str,port:int,password:str):
        self.hostname = hostname
        self.port = port
        self.password = password
        self.connection = None
    
    def __enter__(self):
        self.connection = psycopg2(self.hostname,self.password)
    def __exit__(self):
        self.connection.close()


with DbConnection("chris",5427,"saint") as db:
    pass
        