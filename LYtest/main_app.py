from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.clock import Clock
from datetime import datetime

class ClockApp(BoxLayout):
    def __init__(self, **kwargs):
        super(ClockApp, self).__init__(**kwargs)
        self.label = Label(text='', font_size=50, halign='center')
        self.add_widget(self.label)
        self.orientation = 'horizontal'
        self.opacity = 0  # 初期状態は非表示

        # ClockAppの初期化時にClock.schedule_intervalを呼び出す
        Clock.schedule_interval(self.update_time, 1)

    def on_size(self, instance, value):
        self.rect = Rectangle(pos=self.pos, size=self.size)
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0, 0, 1, 1)
            if self.rect:
                self.rect.pos = self.pos
                self.rect.size = self.size
                self.canvas.before.add(self.rect)

    def update_time(self, dt):
        now = datetime.now()
        time_str = now.strftime("%H:%M:%S")
        self.label.text = time_str

class WeatherApp(BoxLayout):
    def __init__(self, **kwargs):
        super(WeatherApp, self).__init__(**kwargs)
        self.label = Label(text='', font_size=50, halign='center', valign='middle')
        self.add_widget(self.label)
        self.opacity = 0  # 初期状態は非表示

        # WeatherAppの初期化時にClock.schedule_intervalを呼び出す
        Clock.schedule_interval(self.update_weather, 1)

    def on_size(self, instance, value):
        self.rect = Rectangle(pos=self.pos, size=self.size)
        self.canvas.before.clear()
        if self.rect:
            with self.canvas.before:
                Color(1, 0, 0, 1)
                self.rect.pos = (self.center_x - self.rect.size[0] / 2, self.center_y - self.rect.size[1] / 2)
                self.canvas.before.add(self.rect)

    def update_weather(self, dt):
        weather_str = "Sunny"
        self.label.text = weather_str

class ExternalApp(App):
    def build(self):
        # ClockAppとWeatherAppのインスタンスを外部の変数として保持
        self.clock_app = ClockApp(size_hint=(0.5, 1), pos_hint={'x': 0})
        self.weather_app = WeatherApp(size_hint=(0.5, 1), pos_hint={'right': 1})

        # チェックボックスの状態を監視するコールバック関数を定義
        def on_checkbox_active(checkbox, value, app):
            checkbox_id = checkbox.id  # get the id here
            if checkbox_id == 'clock_checkbox':
                app.toggle_feature('ClockApp', value)
            elif checkbox_id == 'weather_checkbox':
                app.toggle_feature('WeatherApp', value)

        layout = FloatLayout()

        clock_checkbox = CheckBox(size_hint=(None, None), size=(150, 50),
                                  color=(1, 0, 0, 1), pos_hint={'x': 0, 'top': 1})
        weather_checkbox = CheckBox(size_hint=(None, None), size=(150, 50),
                                    pos_hint={'right': 1, 'top': 1})

        # Set the id attribute after creating the CheckBox instance
        clock_checkbox.id = 'clock_checkbox'
        weather_checkbox.id = 'weather_checkbox'

        # チェックボックスの状態変化時に呼び出されるコールバック関数を設定
        clock_checkbox.bind(active=lambda checkbox, value: on_checkbox_active(checkbox, value, self))
        weather_checkbox.bind(active=lambda checkbox, value: on_checkbox_active(checkbox, value, self))

        layout.add_widget(clock_checkbox)
        layout.add_widget(weather_checkbox)
        layout.add_widget(self.weather_app)
        layout.add_widget(self.clock_app)

        return layout

    def toggle_feature(self, feature_name, active):
        # feature_nameに基づいて適切なインスタンスを取得し、opacityを変更
        if feature_name == 'ClockApp':
            feature = self.clock_app
        elif feature_name == 'WeatherApp':
            feature = self.weather_app
        else:
            return  # 不明な機能は処理しない

        feature.opacity = 1 if active else 0

if __name__ == '__main__':
    ExternalApp().run()
