from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line, Ellipse
from kivy.clock import Clock
from math import cos, sin, pi
from datetime import datetime


class AnalogClock(Widget):
    def __init__(self, **kwargs):
        super(AnalogClock, self).__init__(**kwargs)
        self.size = (300, 300)
        self.center = (self.width / 2, self.height / 2)
        self.update_clock()  # 初期描画
        Clock.schedule_interval(self.update_clock, 1)  # 1秒ごとに時計を更新

    def update_clock(self, *args):
        self.canvas.clear()  # キャンバスをクリア

        # 時計盤を描画
        with self.canvas:
            Ellipse(pos=self.pos, size=self.size)

        # 針の描画
        now = datetime.now()
        hour_angle = -(now.hour % 12 + now.minute / 60.0) * 30 + 90
        minute_angle = -(now.minute + now.second / 60.0) * 6 + 90
        second_angle = -(now.second) * 6 + 90

        # 時針
        hour_length = self.width / 4
        hour_x = self.center_x + hour_length * cos(pi / 180.0 * hour_angle)
        hour_y = self.center_y + hour_length * sin(pi / 180.0 * hour_angle)
        Line(points=[self.center_x, self.center_y, hour_x, hour_y], width=5, cap='round', joint='round')

        # 分針
        minute_length = self.width / 3
        minute_x = self.center_x + minute_length * cos(pi / 180.0 * minute_angle)
        minute_y = self.center_y + minute_length * sin(pi / 180.0 * minute_angle)
        Line(points=[self.center_x, self.center_y, minute_x, minute_y], width=3, cap='round', joint='round')

        # 秒針
        second_length = self.width / 2.5
        second_x = self.center_x + second_length * cos(pi / 180.0 * second_angle)
        second_y = self.center_y + second_length * sin(pi / 180.0 * second_angle)
        Line(points=[self.center_x, self.center_y, second_x, second_y], width=1, cap='round', joint='round')


class ClockApp(App):
    def build(self):
        return AnalogClock()


if __name__ == '__main__':
    ClockApp().run()
