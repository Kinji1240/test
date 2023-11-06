from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.lang import Builder
from external_clock import ClockApp  # 外部アプリのインポート
from external_weather import WeatherApp  # 天気アプリのインポート

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
