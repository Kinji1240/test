import mysql.connector

# MySQL接続設定
config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'weatherareadb',
    'raise_on_warnings': True
}

# データベースに接続
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

# 気象データ取得（ここでは仮のデータとします）
weather_data = {
    "prefecture": "Tokyo",
    "temperature": 25.5,
    "humidity": 60
}

# データをMySQLに保存
insert_query = ("INSERT INTO weather_data (prefecture, temperature, humidity) "
               "VALUES (%s, %s, %s)")
cursor.execute(insert_query, (weather_data["prefecture"], weather_data["temperature"], weather_data["humidity"]))

# コミットして変更を保存
cnx.commit()

# データの取得
select_query = "SELECT * FROM weather_data"
cursor.execute(select_query)

# 取得したデータの表示
for row in cursor.fetchall():
    print(row)

# 接続を閉じる
cursor.close()
cnx.close()