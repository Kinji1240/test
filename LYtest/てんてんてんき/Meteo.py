import requests
import openmeteo_requests
import requests_cache
from retry_requests import retry
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.clock import Clock
import pandas as pd

class WeatherApp(App):
    def build(self):
        # インスタンス変数を初期化
        self.result_label = Label(text="Weather Data will be displayed here.")

        # レイアウトの作成
        layout = BoxLayout(orientation="vertical")
        layout.add_widget(self.result_label)

        # ボタンの作成
        refresh_button = Button(text="Refresh Weather Data", on_press=self.refresh_data)
        layout.add_widget(refresh_button)

        return layout

    def get_weather_data(self, latitude, longitude):
        # Open-Meteo APIの設定
        cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
        retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
        openmeteo = openmeteo_requests.Client(session=retry_session)

        # APIリクエスト
        url = "https://customer-api.open-meteo.com/v1/forecast"
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m",
            "daily": ["weather_code", "temperature_2m_max", "temperature_2m_min"],
            "timezone": "Asia/Tokyo"
        }
        responses = openmeteo.weather_api(url, params=params)

        return responses

    def refresh_data(self, instance):
        # スクリプトの中身をここに移動
        latitude = 35.6895  # 例として東京の緯度
        longitude = 139.6917  # 例として東京の経度

        response = self.get_weather_data(latitude, longitude)[0]
        current = response.Current()
        current_temperature_2m = current.Variables(0).Value()

        daily = response.Daily()
        daily_weather_code = daily.Variables(0).ValuesAsNumpy()
        daily_temperature_2m_max = daily.Variables(1).ValuesAsNumpy()
        daily_temperature_2m_min = daily.Variables(2).ValuesAsNumpy()

        daily_data = {"date": pd.date_range(
            start=pd.to_datetime(daily.Time(), unit="s"),
            end=pd.to_datetime(daily.TimeEnd(), unit="s"),
            freq=pd.Timedelta(seconds=daily.Interval()),
            inclusive="left"
        )}
        daily_data["weather_code"] = daily_weather_code
        daily_data["temperature_2m_max"] = daily_temperature_2m_max
        daily_data["temperature_2m_min"] = daily_temperature_2m_min

        daily_dataframe = pd.DataFrame(data=daily_data)

        # 天気、最高気温、最低気温を表示
        result_text = (
            f"Current Temperature: {current_temperature_2m}\n\n"
            f"Weather Data:\n{daily_dataframe[['date', 'weather_code', 'temperature_2m_max', 'temperature_2m_min']]}\n\n"
            f"Weather Meaning: {get_weather_meaning(daily_weather_code[0])}"
        )
        self.result_label.text = result_text

if __name__ == '__main__':
    WeatherApp().run()
