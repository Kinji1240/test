from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle

import csv
import japanize_kivy
import os

class MainApp(App):
    def build(self):
        layout = GridLayout(cols=1, spacing=10, padding=10)

        # タイトルのラベル
        title_label = Label(
            text="朝の目覚めにこのシステム",
            font_size=24,
            size_hint_y=None,
            height=50,
            halign="center",
        )

        # サブタイトルのラベル
        subtitle_label = Label(
            text="Morning Pi",
            font_size=16,
            size_hint_y=None,
            height=50,
            halign="center",
        )

        button = Button(text="実行", size_hint=(None, None))
        button.bind(on_press=self.launch_main2)

        layout.add_widget(Label())  # 上部の余白用
        layout.add_widget(title_label)
        layout.add_widget(subtitle_label)
        layout.add_widget(button)

        return layout

    def launch_main2(self, instance):
        # main2.pyを実行
        os.system("python main2.py")
        

    def on_start(self):
        # CSVファイルから背景色を取得
        color = self.get_background_color_from_csv("color_settings.csv")
        self.set_background_color(color)

    def get_background_color_from_csv(self, csv_file):
        with open(csv_file, "r") as file:
            reader = csv.reader(file)
            next(reader)  # ヘッダ行をスキップ
            for row in reader:
                try:
                    green_value = float(row[1])
                    break  # 最初の行の値を使用
                except ValueError:
                    pass
        return (0, green_value, 0)

    def set_background_color(self, color):
        self.root.canvas.before.clear()  # 既存の背景をクリア
        with self.root.canvas.before:
            Color(*color)
            Rectangle(pos=self.root.pos, size=self.root.size)

if __name__ == "__main__":
    MainApp().run()