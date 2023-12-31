from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.app import App
from kivy.clock import Clock
import requests
import japanize_kivy
from openmeteo_sdk import OpenMeteo
from retry_requests import retry
import pandas as pd
import requests_cache



class WeatherApp(App):
    def build(self):
        # ルート レイアウトを作成
        self.root_layout = BoxLayout(orientation='vertical')

        # 天気情報のための BoxLayout を作成
        self.weather_layout = BoxLayout()
        self.root_layout.add_widget(self.weather_layout)

        # 初回のデータ取得と定期的な更新をスケジュール
        self.update_weather_data()
        Clock.schedule_interval(lambda dt: self.update_weather_data(), 3600)  # 1時間ごとに更新

        return self.root_layout

    def update_weather_data(self, dt=None):
        # CSVファイルから座標を読み込む
        coordinates_df = pd.read_csv("test/LYtest/47都道府県IDOKEIDO-UTF8.csv", encoding="UTF-8")

        # 例として、最初の都道府県の座標を使用する
        user_latitude = coordinates_df.loc[5, "緯度"]
        user_longitude = coordinates_df.loc[5, "経度"]

        cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
        retry_session = retry(cache_session, retries=5, backoff_factor=0.2)

        # OpenMeteoクラスを使用するように変更
        openmeteo = OpenMeteo(session=retry_session)

        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": user_latitude,
            "longitude": user_longitude,
            "daily": ["temperature_2m_max", "temperature_2m_min", "weather_code"],
            "timezone": "Asia/Tokyo"
        }

        try:
            response = openmeteo.weather_api(url, params=params)
            print("API Response:", response)

            # レスポンスがリスト形式であれば、最初の要素を取得
            if isinstance(response, list):
                response = response[0]

            weather_data = response.get("daily", {})  # レスポンスから天気情報のデータを取得
            self.update_display(weather_data)

        except Exception as e:
            print(f"Error accessing request URL: {e}")
            print("天気データは利用できません。")

    def update_display(self, weather_data):
        if weather_data:
            time = weather_data.get("time", [])
            max_temperature = weather_data.get("temperature_2m_max", [])
            min_temperature = weather_data.get("temperature_2m_min", [])
            weather_code = weather_data.get("weather_code", [])

            if time and max_temperature and min_temperature and weather_code:
                weekly_data = []  # 指定された日数分のデータを格納するリスト
                for i in range(min(7, len(time))):  # 7日間分のデータを使用
                    day_data = {
                        'day': time[i],
                        'max_temp': max_temperature[i],
                        'min_temp': min_temperature[i],
                        'weather': self.get_weather_meaning(weather_code[i])
                    }
                    weekly_data.append(day_data)

                # 指定された日数分のデータを更新
                self.update_weekly_data(weekly_data)

    def update_weekly_data(self, weekly_data):
        # 指定された日数分のデータをレイアウトに反映
        self.weather_layout.clear_widgets()
        for day_data in weekly_data:
            day_layout = BoxLayout(orientation='vertical', spacing=5)
            dLabel1 = Label()

            day_label = Label(text=day_data['day'], font_size='20sp')
            max_temp_label = Label(text=f"最高気温: {day_data['max_temp']}°C", font_size='20sp')
            min_temp_label = Label(text=f"最低気温: {day_data['min_temp']}°C", font_size='20sp')
            weather_label = Label(text=f"天気: {day_data['weather']}", font_size='20sp')
            dLabel2 = Label()

            # 天気に対応する画像を表示
            weather_image = Image(source=self.get_weather_image(day_data['weather']))
            day_layout.add_widget(dLabel1)
            day_layout.add_widget(day_label)
            day_layout.add_widget(max_temp_label)
            day_layout.add_widget(min_temp_label)
            day_layout.add_widget(weather_label)
            day_layout.add_widget(weather_image)
            day_layout.add_widget(dLabel2)
            self.weather_layout.add_widget(day_layout)

    def get_weather_meaning(self, weather_code):
        if 0 <= weather_code <= 3:
            return "00 - 03 晴れ"
        elif 4 <= weather_code <= 9:
            return "04 - 09 霞、ほこり、砂または煙"
        elif 20 <= weather_code <= 29:
            return "20 - 29 降水、霧、氷霧、または雷雨"
        elif 30 <= weather_code <= 35:
            return "30 - 35 塵嵐、砂嵐"
        elif 36 <= weather_code <= 39:
            return "36 - 39 吹雪または吹雪"
        elif 40 <= weather_code <= 49:
            return "40 - 49 霧または氷"
        elif 50 <= weather_code <= 59:
            return "50 - 59 霧または氷"
        elif 60 <= weather_code <= 69:
            return "60 - 69 霧雨"
        elif 70 <= weather_code <= 79:
            return "70 - 79 雨"
        elif 80 <= weather_code <= 89:
            return "80 - 89 にわか降水"
        elif 90 <= weather_code <= 99:
            return "90 - 99 降雪またはしんしゃく"
        elif 100 <= weather_code <= 199:
            return "100 - 199 あられ"
        else:
            return "不明な天気"

    def get_weather_image(self, weather_meaning):
        if "晴れ" in weather_meaning:
            return "sunny.png"
        elif "霞" in weather_meaning or "ほこり" in weather_meaning or "砂または煙" in weather_meaning:
            return "haze.png"
        elif "降水" in weather_meaning or "霧" in weather_meaning or "氷霧" in weather_meaning or "雷雨" in weather_meaning:
            return "rainy.png"
        elif "塵嵐" in weather_meaning or "砂嵐" in weather_meaning:
            return "dust_storm.png"
        elif "吹雪" in weather_meaning or "吹雪" in weather_meaning:
            return "blizzard.png"
        elif "霧" in weather_meaning or "氷霧" in weather_meaning:
            return "foggy.png"
        elif "霧" in weather_meaning or "氷霧" in weather_meaning:
            return "foggy.png"
        elif "霧雨" in weather_meaning:
            return "drizzle.png"
        elif "雨" in weather_meaning:
            return "rainy.png"
        elif "にわか降水" in weather_meaning:
            return "shower.png"
        elif "降雪" in weather_meaning or "しんしゃく" in weather_meaning:
            return "snowy.png"
        elif "あられ" in weather_meaning:
            return "hail.png"
        else:
            return "unknown.png"

if __name__ == '__main__':
    WeatherApp().run()
