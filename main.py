import pymysql.cursors
import config

#connect using pymysql
connection = pymysql.connect(host=config.hostc,
                             user=config.userc,
                             password=config.passwordc,
                             database=config.databasec,
                             cursorclass=pymysql.cursors.DictCursor)

try:
    connection.ping()
    logging.info("DB connection established")
except:
    logging.warning("DB connection issue")

with connection:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `username`,`email`, `password` FROM `user`"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        logging.info("Main worked")
        
        
#connection.close() #unnecessary

