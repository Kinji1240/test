from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import requests
import japanize_kivy


class WeatherApp(App):
    def build(self):

        user_latitude = 43.06819
        user_longitude = 141.32346

        # Open Meteo APIからデータを取得
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": user_latitude,  # ご自身の緯度に変更
            "longitude": user_longitude,  # ご自身の経度に変更
            "hourly": "temperature_2m",
            "daily": ["weather_code", "temperature_2m_max", "temperature_2m_min"],
            "timezone": "Asia/Tokyo"
        }
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()

            # データの構造を確認する
            print(data)

            # データの構造に基づいて適切にアクセスする
            temperature = data["hourly"]["temperature_2m"][0]
            weather_code = data["daily"]["weather_code"][0]

            # KivyアプリケーションのUIを構築
            layout = BoxLayout(orientation='vertical')
            temperature_label = Label(text=f"現在の気温: {temperature} ℃")
            weather_label = Label(text=f"天気コード: {weather_code}")

            # レイアウトにウィジェットを追加
            layout.add_widget(temperature_label)
            layout.add_widget(weather_label)

            return layout
        else:
            return Label(text=f"エラー: {response.status_code}")

if __name__ == '__main__':
    WeatherApp().run()
