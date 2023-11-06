from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config


class WeatherApp(BoxLayout):
    def __init__(self, **kwargs):
        super(WeatherApp, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint_x = 0.3  # 幅の割合
        self.weather_label = Label(text='Weather: Sunny', font_size=20, halign='center')
        self.temperature_label = Label(text='Temperature: 25°C', font_size=20, halign='center')
        self.add_widget(self.weather_label)
        self.add_widget(self.temperature_label)

Config.set('graphics', 'resizable', 1)
