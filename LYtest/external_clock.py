from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.clock import Clock
from datetime import datetime
from kivy.graphics import Color, Rectangle  # ColorとRectangleをインポート

class ClockApp(BoxLayout):
    def __init__(self, **kwargs):
        super(ClockApp, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_x = 0.7
        self.label = Label(text='', font_size=50, halign='center')
        self.add_widget(self.label)
        Clock.schedule_interval(self.update_time, 1)
        self.rect = None  # Rectangleオブジェクトを初期化

    def on_size(self, instance, value):
        # ウィジェットのサイズが変更されたら、背景キャンバスを設定
        self.rect = Rectangle(pos=self.pos, size=self.size)
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0, 0, 1, 1)  # 青色のRGBA値
            if self.rect:
                self.canvas.before.add(self.rect)

    def update_time(self, dt):
        now = datetime.now()
        time_str = now.strftime("%H:%M:%S")
        self.label.text = time_str
