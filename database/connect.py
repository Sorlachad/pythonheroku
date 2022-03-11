import psycopg2

db_host="localhost"
db_name="Product"
db_user="postgres"
db_pass="time4748"
port=5555

username = "kfjhlwtuirooci"
password = "6e4530a0a7a5bc4f42c32165555d25d40a0b50450aa5fecdbed02e02cafbdbef"
database = "d4rehjq5vhqc06"
hostname = "ec2-3-222-49-168.compute-1.amazonaws.com"
port2 = 5432
conhero = psycopg2.connect(
    database = database,
    user = username,
    password = password,
    host = hostname,
    port = port2
)

conn_str = (
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=LAPTOP-6B2LAJFC;'
    r'DATABASE=User;'
    r'Trusted_Connection=yes;'
)
sqlDbconn = ''

sqlDbconn_product = psycopg2.connect(dbname=database,user=username,password=password,host=hostname,port=port2)