import requests
from bs4 import BeautifulSoup

# 天気情報を取得するURL
url = 'https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json'

# HTTPリクエストを送信し、HTMLデータを取得
response = requests.get(url)

if response.status_code == 200:
    # HTMLデータを解析
    soup = BeautifulSoup(response.text, 'html.parser')

    # 天気情報
    weather_info = soup.find('p', class_='forecast').text.strip()

    # 気圧情報
    pressure_info = soup.find('td', class_='pressure').text.strip()

    # 湿度情報
    humidity_info = soup.find('td', class_='humidity').text.strip()

    # 結果を表示
    print("大阪の天気:", weather_info)
    print("気圧:", pressure_info)
    print("湿度:", humidity_info)

else:
    print("HTTPリクエストが失敗しました。ステータスコード:", response.status_code)