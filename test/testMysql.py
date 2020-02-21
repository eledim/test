import mysql.connector
conn = mysql.connector.connect(user='root', password='1234][po', database='forum')
cursor = conn.cursor()
cursor.execute('insert into user (id, userid,username) values (%s, %s,%s)', ['2', '2','chen'])
cursor.rowcount
conn.commit()
cursor.close()