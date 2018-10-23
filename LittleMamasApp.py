import mysql.connector
from mysql.connector import errorcode
import boto3
import time

endpoint = 'null'
client = boto3.client('rds', region_name='eu-west-1')
while endpoint == 'null':
    response = client.describe_db_instances()
    databases = response['DBInstances']
    for database in databases:
        if database['DBName'] == 'dev_mamas_rds':
            endpoint = database['Endpoint']['Address']
    print("Waiting 1 min...")
    time.sleep(60)

mydb = mysql.connector.connect(
  host=endpoint,
  user="admin",
  passwd="9aDrG}GK$>[#E4A"
)

cursor = mydb.cursor()
DB_NAME = "MAMAS_DB"
def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exist.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        mydb.database = DB_NAME
    else:
        print(err)
        exit(1)
