import requests
from bs4 import BeautifulSoup

# 気象庁のウェブサイトのURL
url = "https://www.jma.go.jp/jp/yoho/"

# URLからHTMLデータを取得
response = requests.get(url)

# HTTPリクエストが成功したか確認
if response.status_code == 200:
    # レスポンスのテキストを取得
    html = response.text

    # BeautifulSoupを使用してHTMLを解析
    soup = BeautifulSoup(html, "html.parser")

    # 例：天気情報の部分を抽出
    weather_info = soup.find("div", class_="forecast-today")
    
    if weather_info:
        # 天気情報を表示
        print("天気情報:")
        print(weather_info.text.strip())
    else:
        print("天気情報が見つかりませんでした。")

else:
    print("HTTPリクエストが失敗しました。ステータスコード:", response.status_code)