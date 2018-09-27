import mysql.connector

mydb = mysql.connector.connect(
  host="terraform-20180927105136845700000001.comuflukwjwy.eu-west-1.rds.amazonaws.com",
  user="admin",
  passwd="9aDrG}GK$>[#E4A"
)

print(mydb)
