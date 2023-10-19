import tkinter as tk
import requests

def get_weather():
    try:
        # Japan Meteorological AgencyのAPIから天気情報を取得
        url = 'https://www.jma.go.jp/bosai/forecast/data/forecast/270000.json'
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # ここでは大阪の天気情報を取得
        osaka_weather = data['timeSeries'][0]['areas'][0]['weathers'][0]['weather']

        # 取得した天気情報をラベルに表示
        weather_label.config(text=f"大阪の天気: {osaka_weather}")
    except requests.exceptions.RequestException as e:
        weather_label.config(text="天気情報の取得に失敗しました")

# Tkinterウィンドウを作成
window = tk.Tk()
window.title("天気情報")

# 天気情報を表示するラベル
weather_label = tk.Label(window, text="ここに天気情報が表示されます")
weather_label.pack(padx=20, pady=10)

# 天気情報を取得するボタン
get_weather_button = tk.Button(window, text="天気情報を取得", command=get_weather)
get_weather_button.pack(pady=10)

# ウィンドウを表示
window.mainloop()