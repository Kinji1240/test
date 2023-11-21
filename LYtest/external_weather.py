from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock

class WeatherApp(FloatLayout):
    def __init__(self, **kwargs):
        super(WeatherApp, self).__init__(**kwargs)
        self.label = Label(text='Sunny', font_size=50, halign='center', valign='middle')
        self.add_widget(self.label)
        self.opacity = 1

    def on_size(self, instance, value):
        self.label.size = self.size
        self.label.pos = (self.center_x - self.label.size[0] / 2, self.center_y - self.label.size[1] / 2)

class WeatherAppApp(App):
    def build(self):
        return WeatherApp(size_hint=(1, 1), pos_hint={'x': 0, 'y': 0})

if __name__ == '__main__':
    WeatherAppApp().run()
