from kivy.app import App
from kivy.uix.checkbox import CheckBox
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from external_clock import ClockApp
from external_weather import WeatherApp
from kivy.lang import Builder

from kivy.factory import Factory

Factory.register('ClockApp', cls=ClockApp)
Factory.register('WeatherApp', cls=WeatherApp)

kv = '''
FloatLayout:

    BoxLayout:
        orientation: 'horizontal'
        ClockApp:
            id: clock_app
            size_hint: 0.5, 1
            pos_hint: {'x': 0, 'y': 0}

        WeatherApp:
            id: weather_app
            size_hint: 0.5, 1
            pos_hint: {'x': 0.5, 'y': 0}

    CheckBox:
        id: clock_checkbox
        text: 'Show Clock'
        size_hint: None, None
        size: 150, 50
        color: 1, 0, 0, 1
        pos_hint: {'x': 0, 'top': 1}
        on_active: app.toggle_feature('ClockApp', self.active)

    CheckBox:
        id: weather_checkbox
        size_hint: None, None
        size: 150, 50
        pos_hint: {'right': 1, 'top': 1}
        on_active: app.toggle_feature('WeatherApp', self.active)
'''

class ExternalApp(App):
    def build(self):
        return Builder.load_string(kv)

    def toggle_feature(self, feature_name, active):
        print("Toggling Feature:", feature_name, "Active:", active)
        feature_id = feature_name.lower() + "_app"
        if feature_id in self.root.ids:
            feature = self.root.ids[feature_id]
            feature.opacity = 1 if active else 0
        else:
            print(f"Error: {feature_id} not found in root.ids")

if __name__ == '__main__':
    ExternalApp().run()
