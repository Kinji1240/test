from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock

class WeatherApp(FloatLayout):
    def __init__(self, **kwargs):
        super(WeatherApp, self).__init__(**kwargs)
        self.label = Label(text='', font_size=50, halign='center', valign='middle')
        self.add_widget(self.label)
        self.opacity = 1

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

class WeatherAppApp(App):
    def build(self):
        return WeatherApp(size_hint=(1, 1), pos_hint={'x': 0, 'y': 0})

if __name__ == '__main__':
    WeatherAppApp().run()
