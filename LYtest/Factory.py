from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from external_clock import ClockApp
from external_weather import WeatherApp
from kivy.factory import Factory

# ファクトリにクラスを登録
Factory.register('ClockApp', cls=ClockApp)
Factory.register('WeatherApp', cls=WeatherApp)

kv = '''
BoxLayout:
    orientation: 'horizontal'

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
