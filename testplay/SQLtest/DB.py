cursor.execute('SELECT * FROM mytable')
data = cursor.fetchall()
for row in data:
    print(row)