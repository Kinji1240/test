from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
import requests
import japanize_kivy

class WeatherApp(App):
    def build(self):
        self.api_url = "https://api.open-meteo.com/v1/forecast?latitude=34.7&longitude=135.5&daily=temperature_2m_max,temperature_2m_min,weather_code&timezone=Asia%2FTokyo"
        self.data = None

        # ルート レイアウトを作成
        self.root_layout = BoxLayout(orientation='vertical', spacing=10, padding=[10, 50, 10, 10])  # padding を調整

        # ボタン レイアウトを作成
        button_layout = BoxLayout(size_hint_y=None, height='30dp', spacing=10)
        self.root_layout.add_widget(button_layout)

        # ボタンを作成し、ボタン レイアウトに追加
        button_1day = Button(text='1日', size_hint=(None, None), width=60, height=30, on_press=lambda x: self.update_display(1))
        button_3day = Button(text='3日', size_hint=(None, None), width=60, height=30, on_press=lambda x: self.update_display(3))
        button_7day = Button(text='7日', size_hint=(None, None), width=60, height=30, on_press=lambda x: self.update_display(7))
        button_layout.add_widget(button_1day)
        button_layout.add_widget(button_3day)
        button_layout.add_widget(button_7day)

        # 天気情報のための BoxLayout を作成
        self.weather_layout = BoxLayout(size_hint_y=None, height='160dp', spacing=5)
        self.root_layout.add_widget(self.weather_layout)

        # 初回のデータ取得と定期的な更新をスケジュール
        self.update_weather_data()
        Clock.schedule_interval(lambda dt: self.update_weather_data(), 3600)  # 1時間ごとに更新

        return self.root_layout

    def on_start(self):
        # アプリケーションが起動したときにウィンドウの中央に配置する
        Window.bind(on_resize=self.center_layout)
        self.center_layout(Window.width, Window.height)

    def center_layout(self, width, height):
        # ウィンドウの中央に配置する
        self.root_layout.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

    def update_weather_data(self, dt=None):
        response = requests.get(self.api_url)
        data = response.json()
        self.data = data
        self.update_display(1)  # 初回は1日分のデータを表示

    def update_display(self, days):
        if self.data:
            daily_data = self.data.get("daily", {})
            time = daily_data.get("time", [])
            max_temperature = daily_data.get("temperature_2m_max", [])
            min_temperature = daily_data.get("temperature_2m_min", [])
            weather_code = daily_data.get("weather_code", [])

            if time and max_temperature and min_temperature and weather_code:
                weekly_data = []  # 指定された日数分のデータを格納するリスト
                for i in range(min(days, len(time))):  # days とデータの個数の小さい方を使用
                    day_data = {
                        'day': time[i],
                        'max_temp': max_temperature[i],
                        'min_temp': min_temperature[i],
                        'weather': get_weather_meaning(weather_code[i])
                    }
                    weekly_data.append(day_data)

                # 指定された日数分のデータを更新
                self.update_weekly_data(weekly_data)

    def update_weekly_data(self, weekly_data):
        # 指定された日数分のデータをレイアウトに反映
        self.weather_layout.clear_widgets()
        for day_data in weekly_data:
            day_layout = BoxLayout(orientation='vertical', size_hint_y=None, height='160dp', spacing=5)
            day_label = Label(text=day_data['day'], size_hint_y=None, height='30dp')
            max_temp_label = Label(text=f"最高気温: {day_data['max_temp']}°C", size_hint_y=None, height='30dp')
            min_temp_label = Label(text=f"最低気温: {day_data['min_temp']}°C", size_hint_y=None, height='30dp')
            weather_label = Label(text=f"天気: {day_data['weather']}", size_hint_y=None, height='30dp')
            day_layout.add_widget(day_label)
            day_layout.add_widget(max_temp_label)
            day_layout.add_widget(min_temp_label)
            day_layout.add_widget(weather_label)
            self.weather_layout.add_widget(day_layout)

def get_weather_meaning(weather_code):
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
    elif 40 <= weather_code <= 49:
        return "40 - 49 霧または氷霧"
    elif 50 <= weather_code <= 59:
        return "50 - 59 霧雨"
    elif 60 <= weather_code <= 69:
        return "60 - 69 雨"
    elif 70 <= weather_code <= 79:
        return "70 - 79 にわか降水（シャワーではない）"
    elif 80 <= weather_code <= 99:
        return "80 - 99 にわか降水、または現在または直近の雷雨"
    else:
        return "不明"

if __name__ == '__main__':
    WeatherApp().run()
