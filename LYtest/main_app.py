from kivy.app import App
from kivy.uix.checkbox import CheckBox
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from external_clock import ClockApp
from external_weather import WeatherApp

from kivy.config import Config
Config.set('graphics', 'width', '500')  # ウィンドウの幅
Config.set('graphics', 'height', '500')  # ウィンドウの高さ

# ClockApp、WeatherAppのクラスをFactoryに登録
from kivy.factory import Factory
Factory.register('ClockApp', cls=ClockApp)
Factory.register('WeatherApp', cls=WeatherApp)

kv = '''
BoxLayout:
    orientation: 'vertical'
    
    CheckBox:
        id: clock_checkbox
        text: 'Show Clock'
        size_hint: None, None
        size: 150, 50
        color: 0, 0, 0, 1  # 黒色に設定
        on_active: app.toggle_feature('ClockApp', self.active)

    CheckBox:
        id: weather_checkbox
        text: 'Show Weather'
        size_hint: None, None
        size: 150, 50
        color: 0, 0, 0, 1  # 黒色に設定
        on_active: 
            print("Weather CheckBox Active:", self.active)
            app.toggle_feature('WeatherApp', self.active)

    ClockApp:
        id: clock_app
        size_hint: 1, 1
        pos_hint: {'x': 0, 'y': 0}

    WeatherApp:
        id: weather_app
        size_hint: 1, 1
        pos_hint: {'x': 0, 'y': 0}
'''

class ExternalApp(App):
    def build(self):
        return Builder.load_string(kv)

    def toggle_feature(self, feature_name, active):
        print("Toggling Feature:", feature_name, "Active:", active)
        # ClockAppとWeatherAppを表示/非表示に切り替える
        feature = self.root.ids[feature_name.lower() + "_app"]
        feature.opacity = 1 if active else 0

if __name__ == '__main__':
    ExternalApp().run()
