import pymysql.cursors
import config
import logging
import logger_conf
from importlib.metadata import version
#import sys

is_ok = 1
#check pymysql version
pymysql_ver = version('pymysql')
if pymysql_ver == "1.1.1":
    logging.info("PyMySQL version is ok (1.1.1)")
else:
    logging.warning("PyMySQL version differs from expected (" + pymysql_ver + ")")

#check DB connection
logging.info("Testing DB connection")

connection = pymysql.connect(host=config.hostc,
                             user=config.userc,
                             password=config.passwordc,
                             database=config.databasec,
                             cursorclass=pymysql.cursors.DictCursor)
    
try:
    connection.ping()
    logging.info("DB connection established")
except:
    logging.error("DB connection issue")
    is_ok = 0
    sys.exit(1)
    
#checking mysql version
sql = "SELECT @@VERSION;"
cursor = connection.cursor() 
cursor.execute(sql)
result = cursor.fetchone()
#print(result['@@VERSION'])
if result['@@VERSION'] == "9.1.0":
    logging.info("MySQL version is ok (9.1.0)")
else:
    logging.warning("MySQL version differs from expected (" + result['@@VERSION'] + ")")
    

if is_ok == 1:
    logging.info("Tests finished without errors")
else:
    logging.warning("Tests finished with errors")

#sys.exit(0)
