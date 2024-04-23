import mysql.connector
import  mysql
con = mysql.connector.connect(host="localhost",user="siddharth",passwd="sidd@30")
print(con)
if(con):
    print("Connection succesfull")
else:
    print("Connection not established")