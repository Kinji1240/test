from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
from datetime import datetime
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

class ClockApp(BoxLayout):
    def __init__(self, **kwargs):
        super(ClockApp, self).__init__(**kwargs)
        self.label = Label(text='', font_size=50, halign='center')
        self.add_widget(self.label)
        self.orientation = 'horizontal'
        self.opacity = 1

    def on_size(self, instance, value):
        self.rect = Rectangle(pos=self.pos, size=self.size)
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0, 0, 1, 1)
            if self.rect:
                self.canvas.before.add(self.rect)

    def update_time(self, dt):
        now = datetime.now()
        time_str = now.strftime("%H:%M:%S")
        self.label.text = time_str


if __name__ == '__main__':
    from kivy.base import runTouchApp

    layout = FloatLayout()
    clock_app = ClockApp(size_hint=(1, 1), pos_hint={'x': 0, 'y': 0})
    layout.add_widget(clock_app)
    runTouchApp(layout)
