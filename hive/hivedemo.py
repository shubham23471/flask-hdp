import pandas as pd
from pyhive import hive
import socket

hostname = socket.gethostname()
conn = hive.Connection(host=hostname, port=10000)
df = pd.read_sql("select * from datamaking_db.customer", con=conn)
print("OUTPUT FROM FIRST METHOD")
print(df.head())

# the other method
from pyhive import hive
import socket

# host_name = socket.gethostname()
hostname = socket.gethostname()
# hostname = "localhost"
print(hostname)
port = 10000
user = "datamaking"
password = " "
database = "datamaking_db"


def hiveconnection(host_name, port, user, password, database):
    conn = hive.Connection(
        host=hostname,
        port=port,
        username=user,
        password=password,
        database=database,
        auth="CUSTOM",
    )
    cursor = conn.cursor()
    cursor.execute("select * from datamaking_db.customer limit 5")
    result = cursor.fetchall()

    return result


# Call above function
output = hiveconnection(hostname, port, user, password, database)
print("OUPUT FROM THE SECOND METHOD")
print(output)
