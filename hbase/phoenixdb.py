import phoenixdb
import phoenixdb.cursor

database_url =  'http://sandbox-hdp.hortonworks.com:8765/'
conn = phoenixdb.connect(database_url, autocommit=True)

cursor = conn.cursor()
# cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username VARCHAR)")
# cursor.execute("UPSERT INTO users VALUES (?, ?)", (1, 'admin'))
cursor.execute("SELECT * FROM us_population")
print(cursor.fetchall())

# cursor = conn.cursor(cursor_factory=phoenixdb.cursor.DictCursor)
# cursor.execute("SELECT * FROM users WHERE id=1")
# print(cursor.fetchone()['USERNAME'])