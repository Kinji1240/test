from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from datetime import datetime
import math

class AnalogClock(BoxLayout):
    def __init__(self, **kwargs):
        super(AnalogClock, self).__init__(**kwargs)
        
        self.orientation = 'vertical'
        self.center_x = 300
        self.center_y = 300
        self.radius = 200
        self.hand_length = 0.8

        self.hour_hand = Label(text='', font_size=24)
        self.min_hand = Label(text='', font_size=18)
        self.sec_hand = Label(text='', font_size=12)

        self.add_widget(self.hour_hand)
        self.add_widget(self.min_hand)
        self.add_widget(self.sec_hand)

        self.add_widget(Label(text='12', size_hint_y=None, height=30))
        
        clock_layout = BoxLayout(size_hint_y=None, height=400)
        clock_layout.add_widget(Label(text='9', size_hint_x=None, width=30))
        clock_layout.add_widget(self.hour_hand)
        clock_layout.add_widget(self.min_hand)
        clock_layout.add_widget(self.sec_hand)
        clock_layout.add_widget(Label(text='3', size_hint_x=None, width=30))
        self.add_widget(clock_layout)

        self.add_widget(Label(text='6', size_hint_y=None, height=30))

        Clock.schedule_interval(self.update_clock, 1)

    def update_clock(self, dt):
        now = datetime.now()
        hour = now.hour % 12
        minute = now.minute
        second = now.second

        hour_angle = (90 - (hour + minute / 60.0) * 360.0 / 12.0) % 360
        min_angle = (90 - (minute + second / 60.0) * 360.0 / 60.0) % 360
        sec_angle = (90 - second * 360.0 / 60.0) % 360

        self.hour_hand.text = 'H'
        self.hour_hand.pos = self.calculate_hand_position(hour_angle, self.radius)

        self.min_hand.text = 'M'
        self.min_hand.pos = self.calculate_hand_position(min_angle, self.radius)

        self.sec_hand.text = 'S'
        self.sec_hand.pos = self.calculate_hand_position(sec_angle, self.radius)

    def calculate_hand_position(self, angle, radius):
        x = self.center_x + radius * self.hand_length * math.cos(math.radians(angle))
        y = self.center_y + radius * self.hand_length * math.sin(math.radians(angle))
        return x, y

class AnalogClockApp(App):
    def build(self):
        return AnalogClock()

if __name__ == '__main__':
    AnalogClockApp().run()
