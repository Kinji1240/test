from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
import csv
import japanize_kivy
import os
from kivy.config import Config
from kivy.core.window import Window

Config.set('graphics', 'width', 1920)  # ウィンドウの幅
Config.set('graphics', 'height', 1080)  # ウィンドウの高さ

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

        return layout

    def launch_main2(self, instance):
        # main2.pyを実行
        os.system("python button_clock.py")

    def launch_main3(self, instance):
        # main3.pyを実行
        os.system("python weather2.py")
        os.system("python weathersearch.py")

    def launch_main4(self, instance):
        # main3.pyを実行
        os.system("python Calendar.py")

    def launch_main5(self, instance):
        # main3.pyを実行
        os.system("python haikei.py")

    def launch_main6(self, instance):
        # main3.pyを実行
        os.system("kakuninn.py")

    def launch_main2(self, instance):
        # main2.pyを実行
        os.system("python MAINSYS/syokihaiti.py")

    def on_start(self):
        # CSVファイルから背景色と文字の色を取得
        background_color, title_color, subtitle_color = self.get_colors_from_csv("MAINSYS/CSV/color_settings.csv")
        self.set_background_color(background_color)
        self.set_text_color(title_color, subtitle_color)
     
    def on_window_resize(self, instance, width, height):
        # ウィンドウサイズが変更されたときに呼ばれるメソッド
        self.set_background_color(self.background_color, width, height)


    def get_colors_from_csv(self, csv_file):
        background_color = (1, 1, 1)  # デフォルトの背景色（白）
        title_color = (0, 0, 0)  # デフォルトのタイトル文字色（黒）
        subtitle_color = (0, 0, 0)  # デフォルトのサブタイトル文字色（黒）

        with open(csv_file, "r") as file:
            reader = csv.reader(file)
            # 1行目をスキップ
            next(reader)
            for row in reader:
                try:
                    background_color = (float(row[0]), float(row[1]), float(row[2]))
                    if len(row) > 5:  # CSVファイルにタイトルとサブタイトルの色情報が含まれているか確認
                        title_color = (float(row[3]), float(row[4]), float(row[5]))
                    if len(row) > 8:  # CSVファイルにサブタイトルの色情報が含まれているか確認
                        subtitle_color = (float(row[6]), float(row[7]), float(row[8]))
                    break  # 最初の行の値を使用
                except ValueError:
                    pass
        return background_color, title_color, subtitle_color

    def set_background_color(self, color):
        self.root.canvas.before.clear()  # 既存の背景をクリア
        with self.root.canvas.before:
            Color(*color)
            Rectangle(pos=self.root.pos, size=self.root.size)

    def set_text_color(self, title_color, subtitle_color):
        # タイトルとサブタイトルの文字色を変更
        self.root.children[0].color = title_color
        self.root.children[1].color = title_color  # タイトルの文字色を変更
        self.root.children[2].color = title_color  # サブタイトルの文字色を変更
        self.root.children[3].color = title_color
        self.root.children[4].color = title_color
        self.root.children[5].color = title_color # タイトルの文字色を変更

if __name__ == "__main__":
    MainApp().run()