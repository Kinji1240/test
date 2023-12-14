from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Ellipse, Color
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
import math

class CircleApp(App):
    def build(self):
        # CircleWidgetを先に作成
        circle_widget = CircleWidget()

        # 数字のレイアウト
        number_layout = RelativeLayout(size=(200, 200), pos=(circle_widget.center_x - 100, circle_widget.center_y - 100))

        # 数字を描写
        val = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        for i in range(12):
            angle = math.radians(-(i * (360 / 12) - 90))  # 円周上の角度を計算 (マイナス符号と90度の補正を追加)
            x = 100 * math.cos(angle)  # 数字の位置を計算
            y = 100 * math.sin(angle)

            label = Label(text=str(val[i]), pos=(x, y), font_size=20, color=(1, 0, 0, 1))
            number_layout.add_widget(label)

        # これを追加
        number_layout.bind(pos=circle_widget.update_circle)
        number_layout.bind(size=circle_widget.update_circle)

        # 数字のレイアウトをCircleWidgetの子として追加
        circle_widget.add_widget(number_layout)

        return circle_widget

class CircleWidget(Widget):
    def __init__(self, **kwargs):
        super(CircleWidget, self).__init__(**kwargs)

        # 円を描写
        with self.canvas:
            Color(1, 1, 1, 1)  # 赤色
            self.circle = Ellipse(pos=(self.center_x - 100, self.center_y - 100), size=(200, 200))

    def update_circle(self, *args):
        # 画面の中央に円を配置し直す
        self.circle.pos = (self.center_x - 100, self.center_y - 100)

if __name__ == '__main__':
    CircleApp().run()
