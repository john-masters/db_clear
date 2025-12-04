import os

import MySQLdb
from dotenv import load_dotenv

load_dotenv()
db_schema = os.getenv("DB_SCHEMA")
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_passwd = os.getenv("DB_PASSWD")


db = MySQLdb.connect(host=db_host, user=db_user, passwd=db_passwd, db=db_schema)
cur = db.cursor()

sql = """SELECT
        concat("kill ", id, ";")
    FROM
        information_schema.processlist
    WHERE
        db = 'mystro'
            AND state = 'Copying to tmp table'
            AND ID <> CONNECTION_ID();"""


cur.execute(sql)
for row in cur.fetchall():
    print("executing this statement: ", row[0])
    cur.execute(row[0])
db.close()
print("finished")
