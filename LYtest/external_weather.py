from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock

class WeatherApp(Label):
    def __init__(self, **kwargs):
        super(WeatherApp, self).__init__(**kwargs)
        self.label = Label(text='', font_size=50, halign='center')
        self.add_widget(self.label)
        self.opacity = 1

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

if __name__ == '__main__':
    from kivy.base import runTouchApp

    layout = FloatLayout()
    weather_app = WeatherApp(size_hint=(1, 1), pos_hint={'x': 0, 'y': 0})
    layout.add_widget(weather_app)
    runTouchApp(layout)

