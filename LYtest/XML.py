import requests
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from datetime import datetime
import japanize_kivy

class WeatherApp(App):
    def build(self):
        self.api_url = "https://api.open-meteo.com/v1/forecast?latitude=34.7&longitude=135.5&hourly=temperature_2m,weather_code&timezone=Asia%2FTokyo"
        self.data = None
        self.label = Label()
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.label)
        # 最初のデータ取得と更新関数の呼び出しをスケジュール
        self.update_weather_data()
        Clock.schedule_interval(self.update_weather_data, 3600)  # 1時間ごとに更新
        return layout

    def update_weather_data(self, dt=None):
        response = requests.get(self.api_url)
        data = response.json()
        self.data = data
        self.update_display()

    def update_display(self):
        if self.data:
            hourly_data = self.data.get("hourly", {})
            time = hourly_data.get("time", [])
            temperature_2m = hourly_data.get("temperature_2m", [])
            weather_code = hourly_data.get("weather_code", [])

            if time and temperature_2m and weather_code:
                current_time = datetime.now()
                current_time = current_time.replace(minute=0, second=0)  # 分と秒を0に設定
                nearest_time = min(time, key=lambda x: abs(current_time - datetime.fromisoformat(x)))  # 最も近い時刻を探す

                current_temperature = temperature_2m[time.index(nearest_time)]
                current_weather_code = weather_code[time.index(nearest_time)]
                current_weather = get_weather_meaning(current_weather_code)

                # 一日の時間枠を取得
                start_of_day = current_time.replace(hour=0, minute=0, second=0)
                end_of_day = current_time.replace(hour=23, minute=59, second=59)

                # 一日の時間枠内での最高気温と最低気温を計算
                max_temperature = max(temperature_2m[time.index(t)] for t in time if start_of_day <= datetime.fromisoformat(t) <= end_of_day)
                min_temperature = min(temperature_2m[time.index(t)] for t in time if start_of_day <= datetime.fromisoformat(t) <= end_of_day)

                label_text = f"Time: {nearest_time}\nTemperature: {current_temperature}°C\nWeather: {current_weather}\n"
                label_text += f"Max Temperature: {max_temperature}°C\nMin Temperature: {min_temperature}°C"
            else:
                label_text = "データなし"
        else:
            label_text = "データなし"

        self.label.text = label_text

def get_weather_meaning(weather_code):
    # 新しい天気コードと意味の対応表
    weather_codes = {
        0: "晴れ (No cloud at any level)",
        1: "曇り (Partly cloudy - Scattered or broken)",
        2: "吹雪 (Continuous layer(s) of blowing snow)",
        3: "砂嵐、ほこり嵐、または吹雪 (Sandstorm, duststorm, or blowing snow)",
        4: "霧、濃いほこり、またはもや (Fog, thick dust or haze)",
        5: "霧雨 (Drizzle)",
        6: "雨 (Rain)",
        7: "雪、または雨と雪が混じる (Snow, or rain and snow mixed)",
        8: "にわか雨 (Shower(s))",
        9: "雷雨 (Thunderstorm(s))"
    }

    return weather_codes.get(weather_code, "不明")

if __name__ == '__main__':
    WeatherApp().run()
