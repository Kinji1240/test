from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.lang import Builder
from external_clock import ClockApp  # 外部アプリのインポート
from external_weather import WeatherApp  # 天気アプリのインポート

from kivy.config import Config
Config.set('graphics', 'width', '1920')  # ウィンドウの幅
Config.set('graphics', 'height', '1080')  # ウィンドウの高さ


kv = '''
BoxLayout:
    orientation: 'horizontal'
    ClockApp:
    WeatherApp:
'''

class ExternalApp(App):
    def build(self):
        return Builder.load_string(kv)

if __name__ == '__main__':
    ExternalApp().run()
