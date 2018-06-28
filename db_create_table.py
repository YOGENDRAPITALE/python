import pymysql
try:
    conn=pymysql.connect(user='root',password='',host='localhost',port=3306,db="python_tutorial")
    cursor=conn.cursor()

    sql_create_table= """Create Table Person(
                        ID INT NOT NULL,
                        FIRST_NAME CHAR(20) NOT NULL,
                        LAST_NAME CHAR(20),
                        AGE INT,
                        SEX CHAR(1),
                        PRIMARY KEY(ID)
                        )"""
    cursor.execute(sql_create_table)
    conn.close()
    
except:
    print("Error Occured!")
                                 
