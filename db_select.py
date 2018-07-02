import pymysql
try:
        conn=pymysql.connect(user='root',password='',host='localhost',port=3306,db="python_tutorial")
        cursor=conn.cursor()
        cursor.execute("select * from employee")
       # cursor.execute("select First_Name from employee where id=5")
        for row in cursor:
                print("-----------")
                print("Id is:",row[0])
                print("First Name is:",row[1])
                print("Last Name is:",row[2])
                print("Age Name is:",row[3])
                print(row)             
except:
        print("Error Occured!")



