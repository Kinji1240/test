from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from datetime import datetime

class ClockApp(BoxLayout):  # BoxLayoutのサブクラスとしてClockAppを定義
    def __init__(self, **kwargs):
        super(ClockApp, self).__init__(**kwargs)
        self.orientation = 'horizontal'  # レイアウトを水平に配置
        self.label = Label(text='', font_size=50, halign='center')
        self.add_widget(self.label)
        Clock.schedule_interval(self.update_time, 1)

    def update_time(self, dt):
        now = datetime.now()
        time_str = now.strftime("%H:%M:%S")
        self.label.text = time_str
