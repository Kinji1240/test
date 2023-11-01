from curses.textpad import rectangle
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
import os
import japanize_kivy

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

        layout.add_widget(title_label)
        layout.add_widget(Widget())  # 上部の余白用
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

    def on_start(self):
        # CSVファイルから背景色を取得
        color = self.get_background_color_from_csv("MAINSYS/CSV/color_settings.csv")
        self.set_background_color(color)

    def get_background_color_from_csv(self, csv_file):
        with open(csv_file, "r") as file:
            reader = csv.reader(file)
            next(reader)  # ヘッダ行をスキップ
            for row in reader:
                try:
                    red_value = float(row[0])
                    green_value = float(row[1])
                    blue_value = float(row[2])
                    break  # 最初の行の値を使用
                except ValueError:
                    pass
        return (red_value, green_value, blue_value)

    def set_background_color(self, color):
        self.root.canvas.before.clear()  # 既存の背景をクリア
        with self.root.canvas.before:
            Color(*color)
            rectangle(pos=self.root.pos, size=self.root.size)

if __name__ == "__main__":
    MainApp().run()