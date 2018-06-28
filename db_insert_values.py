import pymysql
try:
    conn=pymysql.connect(user='root',password='',host='localhost',port=3306,db="python_tutorial")
    cursor=conn.cursor()

    cursor.execute("Insert into person(ID ,FIRST_NAME ,LAST_NAME ,AGE,SEX )  Values('4','Ria','Patil','22','F');")
    conn.commit()
    conn.close()
    
except:
    print("Error Occured!")
                               
