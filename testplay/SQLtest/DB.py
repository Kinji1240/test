import sqlite3

# SQLiteデータベースに接続
conn = sqlite3.connect("mydatabase.db")

# カーソルを取得
cursor = conn.cursor()

# テーブルを作成
cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        published_date TEXT
    )
""")

# データを挿入
cursor.execute("INSERT INTO books (title, author, published_date) VALUES (?, ?, ?)", ("Sample Book", "John Doe", "2023-10-25"))

# 変更を保存
conn.commit()

# 接続を閉じる
conn.close()
