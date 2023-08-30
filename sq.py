import mysql.connector
file=mysql.connector.connect(host="root",user="Pratham",passwd="12345678",database="jf")
if file.is_connected()==False:
    print("Error")
else:
    cursor.execute("SElect * from main")