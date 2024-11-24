import pymysql.cursors
import config

#connect using pymysql
connection = pymysql.connect(host=config.hostc,
                             user=config.userc,
                             password=config.passwordc,
                             database=config.databasec,
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `username`,`email`, `password` FROM `user`"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        
        
#connection.close() #unnecessary

