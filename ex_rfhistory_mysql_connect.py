import mysql.connector

mydb = mysql.connector.connect(host="0.0.0.0",user="superuser",passwd="passw0rd",database="UIPSR")
cursor = mydb.cursor()
cursor.execute("SELECT Execution_Html from TB_EXECUTION order by Execution_Id desc LIMIT 500;")
cursor.execute("SELECT Execution_Id, Test_Name, Test_Status, Test_Tag from TB_TEST WHERE Execution_Id=%s" % eid)
cursor.execute("SELECT Execution_Html from TB_EXECUTION WHERE Execution_Id=%s;" % eid)
data = cursor.fetchall()