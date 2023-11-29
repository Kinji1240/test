import openmeteo_requests
import requests_cache
from retry_requests import retry
import pandas as pd
import numpy as np
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt

class WeatherApp(App):
    def build(self):
        # Open-Meteo APIクライアントのセットアップ（キャッシュとエラー時のリトライを含む）
        cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
        retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
        openmeteo = openmeteo_requests.Client(session=retry_session)

        # 必要な気象変数がすべてここにリストされていることを確認
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": 52.52,
            "longitude": 13.41,
            "hourly": "temperature_2m"
        }
        responses = openmeteo.weather_api(url, params=params)

        # 最初の場所を処理。複数の場所や気象モデルの場合はforループを追加します
        response = responses[0]

        # 時間別のデータを処理。変数の順序はリクエストと同じである必要があります
        hourly = response.Hourly()
        hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy().flatten()

        # DateはすでにNumPyの配列になっている
        date = pd.to_datetime(hourly.Time(), unit="s")

        # デバッグのためにデータの形状と値を表示
        print("Before plotting:")
        print("Date shape:", date.shape)
        print("Temperature shape:", hourly_temperature_2m.shape)
        print("Date values:", date)
        print("Temperature values:", hourly_temperature_2m)

        # Matplotlibの図を作成し、気温データをプロットする
        fig, ax = plt.subplots()

        # プロット前に形状を再度表示
        print("Before ax.plot:")
        print("Date shape:", date.shape)
        print("Temperature shape:", hourly_temperature_2m.shape)

        ax.plot(date, hourly_temperature_2m, label="Temperature (2m)")
        ax.set_xlabel("Date")
        ax.set_ylabel("Temperature (°C)")
        ax.legend()

        # ...

if __name__ == '__main__':
    WeatherApp().run()
