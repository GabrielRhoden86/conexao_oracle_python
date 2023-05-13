import oracledb
import os
oracledb.init_oracle_client()

un = os.environ.get('PYTHON_USERNAME',"NOC_PROJETOS")
pw = os.environ.get('PYTHON_PASSWORD',"X;W2izyd")
cs = os.environ.get('PYTHON_CONNECTSTRING',"10.240.47.114/SIGITM")

with oracledb.connect(user=un, password=pw, dsn=cs) as connection:
    with connection.cursor() as cursor:
        sql = """select * from SIGITM3.tipos_rede_tc"""
        for r in cursor.execute(sql):
            print(r)



