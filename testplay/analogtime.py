from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from kivy.clock import Clock
from datetime import datetime
import math

class AnalogClock(Widget):
    def __init__(self, **kwargs):
        super(AnalogClock, self).__init__(**kwargs)
        self._update_clock()
        Clock.schedule_interval(self._update_clock, 1)  # 毎秒アップデート

    def _update_clock(self, *args):
        self.canvas.clear()
        with self.canvas:
            # 時計の中心
            Color(0, 0, 0)
            Ellipse(pos=(self.center_x - 10, self.center_y - 10), size=(20, 20))

            # 時計のふち
            Color(0.7, 0.7, 0.7)  # グレー
            Ellipse(pos=(self.center_x - self.width * 0.48, self.center_y - self.width * 0.48),
                    size=(self.width * 0.96, self.width * 0.96), angle_end=360)

            # 時刻のメモリ
            for i in range(12):
                angle = math.radians(30 * i - 90)
                x1 = self.center_x + self.width * 0.42 * math.cos(angle)
                y1 = self.center_y + self.width * 0.42 * math.sin(angle)
                x2 = self.center_x + self.width * 0.45 * math.cos(angle)
                y2 = self.center_y + self.width * 0.45 * math.sin(angle)
                Line(points=[x1, y1, x2, y2], width=2)

                # 数字を追加
                num = i + 1
                x = self.center_x + self.width * 0.35 * math.cos(angle)
                y = self.center_y + self.width * 0.35 * math.sin(angle)
                Color(0, 0, 0)
                self._draw_text(str(num), x, y)

            # 秒針
            current_time = datetime.now()
            japan_time = current_time.astimezone(timezone('Asia/Tokyo'))
            seconds = japan_time.second
            angle = math.radians(6 * seconds - 90)  # 1秒あたり6度
            self._draw_hand(angle, self.center_x, self.center_y, self.width * 0.4, (0, 0, 1))  # 水色

            # 分針
            minutes = japan_time.minute
            angle = math.radians(6 * (minutes + seconds / 60) - 90)
            self._draw_hand(angle, self.center_x, self.center_y, self.width * 0.35, (0, 0, 1))  # 水色

            # 時針
            hours = japan_time.hour
            if hours > 12:
                hours -= 12
            angle = math.radians(30 * (hours + minutes / 60) - 90)
            self._draw_hand(angle, self.center_x, self.center_y, self.width * 0.3, (0, 0, 1))  # 水色

    def _draw_hand(self, angle, x, y, length, color):
        Color(*color)  # 指定された色
        Line(points=[x, y, x + length * math.cos(angle), y + length * math.sin(angle)], width=2)


class AnalogClockApp(App):
    def build(self):
        return AnalogClock()

if __name__ == '__main__':
    from pytz import timezone  # 追加
    from kivy.uix.label import Label  # 追加
    AnalogClockApp().run()