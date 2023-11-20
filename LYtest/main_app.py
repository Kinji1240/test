from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.lang import Builder
from external_clock import ClockApp  # 外部アプリのインポート
from external_weather import WeatherApp  # 天気アプリのインポート

from kivy.config import Config
Config.set('graphics', 'width', '500')  # ウィンドウの幅
Config.set('graphics', 'height', '500')  # ウィンドウの高さ

kv = '''
FloatLayout:
    ClockApp:
        size_hint: 0.5, 1
        pos_hint: {'x': 0, 'y': 0}
    WeatherApp:
        size_hint: 0.5, 1
        pos_hint: {'x': 0.5, 'y': 0}
'''

class ExternalApp(App):
    def build(self):
        return Builder.load_string(kv)

if __name__ == '__main__':
    ExternalApp().run()
