import requests
import xml.etree.ElementTree as ET
from kivy.app import App
from kivy.uix.label import Label

class WeatherApp(App):
    def build(self):
        # 気象庁のデータを取得するURL
        url = "https://www.jma.go.jp/bosai/jmatile/data/forecast/20231107120000_1200.xml"

        # リクエストを送信してXMLデータを取得
        response = requests.get(url)

        # レスポンスが正常であることを確認
        if response.status_code == 200:
            # XMLデータを解析
            xml_data = response.text

            # XMLデータをElementTreeオブジェクトに変換
            root = ET.fromstring(xml_data)

            # タイトル要素を取得
            title_element = root.find(".//Title")
            if title_element is not None:
                title = title_element.text
            else:
                title = "Title not found in XML data."

            # Kivyラベルを作成してタイトルを表示
            label = Label(text=title)
            return label
        else:
            return Label(text="Failed to fetch data from the JMA website. Status code: " + str(response.status_code))

if __name__ == '__main__':
    WeatherApp().run()
