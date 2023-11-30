import pandas as pd
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import requests

class WeatherApp(App):
    def build(self):
        # CSVファイルから座標を読み取る
        coordinates_df = pd.read_csv('test/LYtest/47都道府県IDOKEIDO-UTF8.csv')
        
        if 'latitude' in coordinates_df.columns and 'longitude' in coordinates_df.columns:
            # データの構造を確認
            print(coordinates_df)

            # 最初の行を取得
            first_row = coordinates_df.iloc[0]
            
            user_latitude = first_row['latitude']
            user_longitude = first_row['longitude']

            # Open Meteo APIからデータを取得
            url = "https://api.open-meteo.com/v1/forecast"
            params = {
                "latitude": user_latitude,
                "longitude": user_longitude,
                "hourly": "temperature_2m",
                "daily": ["weather_code", "temperature_2m_max", "temperature_2m_min"],
                "timezone": "Asia/Tokyo"
            }
            response = requests.get(url, params=params)

            if response.status_code == 200:
                data = response.json()

                # データの構造を確認
                print(data)

                # データの構造に基づいて適切にアクセスする
                temperature = data["hourly"]["temperature_2m"][0]
                max_temperature = data["daily"]["temperature_2m_max"][0]
                min_temperature = data["daily"]["temperature_2m_min"][0]
                weather_code = data["daily"]["weather_code"][0]

                # KivyアプリケーションのUIを構築
                layout = BoxLayout(orientation='vertical')
                temperature_label = Label(text=f"現在の気温: {temperature} ℃")
                max_temperature_label = Label(text=f"最高気温: {max_temperature} ℃")
                min_temperature_label = Label(text=f"最低気温: {min_temperature} ℃")
                weather_label = Label(text=f"天気コード: {weather_code}")

                # レイアウトにウィジェットを追加
                layout.add_widget(temperature_label)
                layout.add_widget(max_temperature_label)
                layout.add_widget(min_temperature_label)
                layout.add_widget(weather_label)

                return layout
            else:
                return Label(text=f"エラー: {response.status_code}")
        else:
            return Label(text="エラー: CSVファイルに 'latitude' と 'longitude' の列がありません。")

if __name__ == '__main__':
    WeatherApp().run()
