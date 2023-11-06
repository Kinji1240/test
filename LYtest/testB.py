from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
import csv
import japanize_kivy
import os

class DraggableButton(Button):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)  # タッチをボタンにグラブ
            return True
        return super(DraggableButton, self).on_touch_down(touch)

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            touch.ungrab(self)  # タッチのグラブを解除
            return True
        return super(DraggableButton, self).on_touch_up(touch)

    def on_touch_move(self, touch):
        if touch.grab_current is self:
            self.center_x = touch.x
            self.center_y = touch.y
            return True
        return super(DraggableButton, self).on_touch_move(touch)

class MainApp(App):
    def build(self):
        layout = GridLayout(cols=1, spacing=10, padding=10)

        # タイトルのラベル
        title_label = Label(
            text="ほしい機能を選んでね",
            font_size=24,
            size_hint_y=None,
            height=50,
            halign="center",
        )

        button1 = DraggableButton(text="時間表示設定", size_hint=(None, None))
        button1.bind(on_press=self.launch_main2)

        button2 = DraggableButton(text="天気予報", size_hint=(None, None))
        button2.bind(on_press=self.launch_main3)

        button3 = DraggableButton(text="予定表示", size_hint=(None, None))
        button3.bind(on_press=self.launch_main4)

        button4 = DraggableButton(text="背景設定", size_hint=(None, None))
        button4.bind(on_press=self.launch_main5)

        button5 = DraggableButton(text="確認画面", size_hint=(None, None))
        button5.bind(on_press=self.launch_main6)

        layout.add_widget(Label())  # 上部の余白用
        layout.add_widget(title_label)
        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)
        layout.add_widget(button4)
        layout.add_widget(button5)

        with layout.canvas.before:
            self.background_color = Color(0, 1, 0, 0)  # 青色
            self.background_rect = Rectangle(pos=layout.pos, size=layout.size)

        layout.bind(pos=self.update_background, size=self.update_background)

        return layout

    def launch_main2(self, instance):
        os.system("python button_clock.py")

    def launch_main3(self, instance):
        os.system("python weather2.py")
        os.system("python weathersearch.py")

    def launch_main4(self, instance):
        os.system("python Calendar.py")

    def launch_main5(self, instance):
        os.system("python haikei.py")

    def launch_main6(self, instance):
        os.system("kakuninn.py")

    def on_start(self):
        background_color, title_color, subtitle_color = self.get_colors_from_csv("test\LYtest\__pycache__\color_settings.csv")
        self.set_background_color(background_color)
        self.set_text_color(title_color, subtitle_color)

    def get_colors_from_csv(self, csv_file):
        background_color = (0, 1, 1, 1)
        title_color = (0, 0, 0, 1)
        subtitle_color = (0, 0, 0, 1)

        with open(csv_file, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # ヘッダー行をスキップ
            for row in reader:
                try:
                    background_color = (float(row[0]), float(row[1]), float(row[2]), 1)
                    if len(row) > 5:
                        title_color = (float(row[3]), float(row[4]), float(row[5]), 1)
                    if len(row) > 8:
                        subtitle_color = (float(row[6]), float(row[7]), float(row[8]), 1)
                    break
                except ValueError:
                    pass
        return background_color, title_color, subtitle_color

    def update_background(self, instance, value):
        self.background_rect.pos = instance.pos
        self.background_rect.size = instance.size

    def set_background_color(self, color):
        self.background_color.rgba = color

    def set_text_color(self, title_color, subtitle_color):
        for child in self.root.children:
            if isinstance(child, Label):
                child.color = title_color

if __name__ == "__main__":
    main_app = MainApp()
    main_app.run()
