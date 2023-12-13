import pandas as pd
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import requests
from datetime import datetime
import csv
import japanize_kivy
from kivy.core.window import Window

## インチあたりのピクセル数
pixels_per_inch = 96

# 縦8cm、横15cmのサイズをピクセルに変換
width_cm = 15
height_cm = 8
width_pixels = int(width_cm * pixels_per_inch / 2.54)
height_pixels = int(height_cm * pixels_per_inch / 2.54)

# ウィンドウサイズの指定
Window.size = (width_pixels, height_pixels)

class WeatherApp(App):
    def get_weather_meaning(self, weather_code):
        if 0 <= weather_code <= 3:
            return "晴れ"
        elif 4 <= weather_code <= 9:
            return "霞、ほこり、砂または煙"
        elif 20 <= weather_code <= 29:
            return "降水、霧、氷霧、または雷雨"
        elif 30 <= weather_code <= 35:
            return "塵嵐、砂嵐"
        elif 36 <= weather_code <= 39:
            return "吹雪または吹雪"
        elif 40 <= weather_code <= 49:
            return "霧または氷"
        elif 50 <= weather_code <= 59:
            return "霧または氷"
        elif 60 <= weather_code <= 69:
            return "霧雨"
        elif 70 <= weather_code <= 79:
            return "雨"
        elif 80 <= weather_code <= 89:
            return "にわか降水"
        elif 90 <= weather_code <= 99:
            return "降雪またはしんしゃく"
        elif 100 <= weather_code <= 199:
            return "あられ"
        else:
            return "不明な天気"

    def format_date(self, date_str):
        date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M")
        formatted_date = date_obj.strftime("%Y-%m-%d %H:%M")
        return formatted_date

    def build(self):
        
        fsize = "18"

        layout = BoxLayout(orientation='vertical')
        coordinates_df = pd.read_csv('test\onoD\onoD_csv_list\IDOKEIDO-UTF8.csv')

        if 'latitude' in coordinates_df.columns and 'longitude' in coordinates_df.columns:
            self.selected_data = None

            # BoxLayout を追加して横に並べる
            horizontal_layout = BoxLayout(orientation='horizontal')
            layout.add_widget(horizontal_layout)

            def update_weather(dt):
                # horizontal_layout のウィジェットをクリア
                horizontal_layout.clear_widgets()

                url = "https://api.open-meteo.com/v1/forecast"

                if self.selected_data is None:
                    user_latitude, user_longitude, selected_days = self.loadopt()

                    params = {
                        "latitude": user_latitude,
                        "longitude": user_longitude,
                        "hourly": "temperature_2m",
                        "daily": ["weather_code", "temperature_2m_max", "temperature_2m_min"],
                        "timezone": "Asia/Tokyo"
                    }

                    response = requests.get(url, params=params)

                    data = response.json()
                    hourly_data = data["hourly"]
                    daily_data = data["daily"]

                    # 日数に応じて表示するデータの範囲を調整
                    if selected_days == "1":
                        range_end = 1
                    elif selected_days == "3":
                        range_end = 3
                    else:
                        range_end = 1  # デフォルトは1日

                    for i in range(range_end):
                        date = hourly_data["time"][i*24]
                        formatted_date = self.format_date(date)
                        temperature = hourly_data["temperature_2m"][i]
                        max_temperature = daily_data["temperature_2m_max"][i]
                        min_temperature = daily_data["temperature_2m_min"][i]
                        weather_code = daily_data["weather_code"][i]
                        weather_meaning = self.get_weather_meaning(weather_code)

                        string_to_remove = "2023-"
                        formatted_date = formatted_date.replace(string_to_remove, "")
                        string_to_remove = "00:00"
                        formatted_date = formatted_date.replace(string_to_remove, "")
                        string_to_remove = "-"
                        formatted_date = formatted_date.replace(string_to_remove, "/")

                        # 横に並べて表示するために BoxLayout を使用
                        box = BoxLayout(orientation='vertical')
                        if i == 0:
                            day = "今日"
                        elif i == 1:
                            day = "明日"
                        elif i == 2:
                            day = "明後日"
                        else: day = "" 

                        weather_label = Label(text=day+
                                            f" {formatted_date}\n" 
                                           +f"\n現在の気温: {temperature} ℃\n"
                                           +f"最高気温: {max_temperature} ℃\n"
                                           +f"最低気温: {min_temperature} ℃\n"
                                           +f"天気: {weather_meaning}"
                                           ,font_size=fsize+'sp')
                        

                        # box を horizontal_layout に追加
                        horizontal_layout.add_widget(box)

                        # box に各情報を追加

                        box.add_widget(weather_label)
                        

                else:
                    horizontal_layout.add_widget(Label(text=f"エラー: {response.status_code}"))

            update_weather(dt = 10)
            Clock.schedule_interval(update_weather, 1800)

            return layout
        else:
            return Label(text="エラー: CSVファイルに 'latitude' と 'longitude' の列がありません。")

    def loadopt(self):
        # CSVファイルに緯度・経度・日数を保存するメソッド
        filename = 'test\onoD\onoD_csv_list\onoD_opt.csv'
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)

            idodata = data[3][1]
            keidodata = data[3][2]
            daydata = data[4][1]

        return idodata, keidodata, daydata

if __name__ == '__main__':
    WeatherApp().run()
