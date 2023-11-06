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
        self.layout = GridLayout(cols=1, spacing=10, padding=10)

        # タイトルのラベル
        title_label = Label(
            text="ほしい機能を選んでね",
            font_size=24,
            size_hint_y=None,
            height=50,
            halign="center",
        )

        button1 = Button(text="時間表示設定", size_hint=(None, None))
        button1.bind(on_press=self.launch_main2)

        button2 = Button(text="天気予報", size_hint=(None, None))
        button2.bind(on_press=self.launch_main3)

        button3 = Button(text="予定表示", size_hint=(None, None))
        button3.bind(on_press=self.launch_main4)

        button4 = Button(text="背景設定", size_hint=(None, None))
        button4.bind(on_press=self.launch_main5)

        button5 = Button(text="確認画面", size_hint=(None, None))
        button5.bind(on_press=self.launch_main6)

        self.layout.add_widget(Label())  # 上部の余白用
        self.layout.add_widget(title_label)
        self.layout.add_widget(button1)
        self.layout.add_widget(button2)
        self.layout.add_widget(button3)
        self.layout.add_widget(button4)
        self.layout.add_widget(button5)

        # 背景の設定
        with self.layout.canvas.before:
            self.bg_color = Color(0, 0, 1, 1)  # 背景色（白）
            self.bg_rect = Rectangle(pos=self.layout.pos, size=self.layout.size)

        # ウィンドウサイズ変更時に背景サイズを調整
        self.layout.bind(size=self.adjust_background_size)

        return self.layout

    def adjust_background_size(self, instance, value):
        # 背景のサイズをウィンドウサイズに合わせて調整
        self.bg_rect.size = instance.size

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

    # 他のメソッドの定義...

if __name__ == "__main__":
    MainApp().run()
