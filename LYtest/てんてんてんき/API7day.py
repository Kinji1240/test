import pandas as pd
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.core.window import Window
import requests
import japanize_kivy
from datetime import datetime

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
        layout = BoxLayout(orientation='vertical')
        coordinates_df = pd.read_csv('test/LYtest/47都道府県IDOKEIDO-UTF8.csv')

        if 'latitude' in coordinates_df.columns and 'longitude' in coordinates_df.columns:
            self.selected_data = None
            spinner_values = coordinates_df['都道府県'].tolist()
            spinner = Spinner(text='都道府県を選択', values=spinner_values)

            def on_spinner_change(spinner, text):
                self.selected_data = coordinates_df[coordinates_df['都道府県'] == text].iloc[0]

            spinner.bind(text=on_spinner_change)
            layout.add_widget(spinner)

            # 日数を選択する Spinner を追加
            days_spinner = Spinner(text='日数を選択', values=['1日', '3日'])
            layout.add_widget(days_spinner)

            # BoxLayout を追加して横に並べる
            horizontal_layout = BoxLayout(orientation='horizontal')
            layout.add_widget(horizontal_layout)

            def update_weather_data(dt):
                # horizontal_layout のウィジェットをクリア
                horizontal_layout.clear_widgets()

                url = "https://api.open-meteo.com/v1/forecast"

                if self.selected_data is not None:
                    user_latitude = self.selected_data['latitude']
                    user_longitude = self.selected_data['longitude']
                    selected_days = days_spinner.text  # 選択された日数を取得

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
                        hourly_data = data["hourly"]
                        daily_data = data["daily"]

                        # 日数に応じて表示するデータの範囲を調整
                        if selected_days == '1日':
                            range_end = 1
                        elif selected_days == '3日':
                            range_end = 3
                        else:
                            range_end = 1  # デフォルトは1日

                        for i in range(range_end):
                            date = hourly_data["time"][i * 24]
                            formatted_date = self.format_date(date)
                            temperature = hourly_data["temperature_2m"][i]
                            max_temperature = daily_data["temperature_2m_max"][i]
                            min_temperature = daily_data["temperature_2m_min"][i]
                            weather_code = daily_data["weather_code"][i]
                            weather_meaning = self.get_weather_meaning(weather_code)

                            # 横に並べて表示するために BoxLayout を使用
                            box = BoxLayout(orientation='vertical')
                            date_label = Label(text=f"日付: {formatted_date}")
                            temperature_label = Label(text=f"現在の気温: {temperature} ℃")
                            max_temperature_label = Label(text=f"最高気温: {max_temperature} ℃")
                            min_temperature_label = Label(text=f"最低気温: {min_temperature} ℃")
                            weather_label = Label(text=f"天気: {weather_meaning}")

                            # box を horizontal_layout に追加
                            horizontal_layout.add_widget(box)

                            # box に各情報を追加
                            box.add_widget(date_label)
                            box.add_widget(temperature_label)
                            box.add_widget(max_temperature_label)
                            box.add_widget(min_temperature_label)
                            box.add_widget(weather_label)
                    else:
                        horizontal_layout.add_widget(Label(text=f"エラー: {response.status_code}"))

            update_button = Button(text="天気を更新", size_hint=(None, None))
            update_button.bind(on_press=update_weather_data)
            layout.add_widget(update_button)

            Clock.schedule_interval(update_weather_data, 10)

            return layout
        else:
            return Label(text="エラー: CSVファイルに 'latitude' と 'longitude' の列がありません。")

if __name__ == '__main__':
    WeatherApp().run()
