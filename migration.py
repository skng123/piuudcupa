import pymysql.cursors
import config
import os

path = "\migrations"

try:
    os.chdir(os.getcwd() + path)
    #print(os.getcwd())

except:
    print("Migrations folder not found")
    sys.exit(1)

connection = pymysql.connect(host=config.hostc,
                             user=config.userc,
                             password=config.passwordc,
                             database=config.databasec,
                             cursorclass=pymysql.cursors.DictCursor)
for file in os.listdir():
    file_path = f"{os.getcwd()}\{file}"
    with connection:
        with connection.cursor() as cursor:
            try:
                with open(file_path, 'r') as f:
                    sql = f.read()
                    cursor.execute(sql)
                    result = cursor.fetchone()
                    print(result)
            except:
                print("something bad or already implemented " + file_path)
        
#should also write an entry with which migrations have been completed
#connection.close()
