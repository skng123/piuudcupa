import pymysql.cursors
import config
import os
import logging
import logger_conf
import sys

path = "\migrations"

try:
    os.chdir(os.getcwd() + path)
    #print(os.getcwd())

except:
    logging.error("Migrations folder not found")
    sys.exit(1)
    
logging.info("Performing DB migration")
    
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
    
for file in os.listdir():
    file_path = f"{os.getcwd()}\{file}"
    
    cursor = connection.cursor() 
    sql = "SELECT migration_script_name, exec_date FROM migrations WHERE migration_script_name LIKE \'" + file + "\'"
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        #the migration had already been performed before
        logging.info("Migration already implemented " + file)
    else:
        #the migration needs to be performed
        f = open(file_path, 'r')
        #perform the migration
        sql = f.read()
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
        #add the migration line to the migrations table
        sql = "INSERT INTO migrations (migration_script_name) VALUES (\'" + file + "\')"
        #print(sql)
        cursor.execute(sql)
        #result = cursor.fetchone()
        logging.info("Migration performed " + file)
        connection.commit()
       
print("line 40")
sys.exit(0)
    
#following code doesn't work after 1st iteration
"""
connection = pymysql.connect(host=config.hostc,
                             user=config.userc,
                             password=config.passwordc,
                             database=config.databasec,
                             cursorclass=pymysql.cursors.DictCursor)
for file in os.listdir():
    file_path = f"{os.getcwd()}\{file}"
    print(file_path)
    with connection:
        with connection.cursor() as cursor:
            try:
                #check if the migration has already been performed
                #print("1 " + file)
                sql = "SELECT migration_script_name, exec_date FROM migrations WHERE migration_script_name LIKE \'" + file + "\'"
                #print("2 " + file)
                #print(cursor.description)
                #print(sql)
                cursor.execute(sql)
                #print("3 " + file)
                result = cursor.fetchone()
                #print("4 " + file)
                if result:
                    #the migration had already been performed before
                    print("already implemented " + file)
                else:
                    #the migration needs to be performed
                    try:
                        #perform the migration
                        with open(file_path, 'r') as f:
                            sql = f.read()
                            cursor.execute(sql)
                            result = cursor.fetchone()
                            print(result)
                        #add the migration line to the migrations table
                        sql = "INSERT INTO migrations (migration_script_name) VALUES (\'" + file + "\')"
                        cursor.execute(sql)
                    except:
                        print("something bad " + file_path)
                        continue
            except Exception as e:
                print("DB issue on " + file_path)
                print(e)
                continue
            finally:
                cursor.close()
                
#print("end of script")
#connection.close()
"""