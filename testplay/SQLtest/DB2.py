import sqlite3

# SQLiteデータベースに接続
conn = sqlite3.connect("mydatabase.db")

# カーソルを取得
cursor = conn.cursor()

# データを取得
cursor.execute("SELECT * FROM books")
data = cursor.fetchall()

# データを表示
for row in data:
    print(f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, Published Date: {row[3]}")

# 接続を閉じる
conn.close()