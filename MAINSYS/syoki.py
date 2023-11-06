from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
import csv
import japanize_kivy
import os
from kivy.core.window import Window
from kivy.uix.popup import Popup

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # タイトルのラベル
        title_label = Label(
            text="朝の目覚めにこのシステム",
            font_size=66,
            size_hint_y=None,
            height=500,
            halign="center",
        )

        # サブタイトルのラベル
        subtitle_label = Label(
            text="Morning Pi",
            font_size=51,
            size_hint_y=None,
            height=100,
            halign="center",
        )

        layout.add_widget(Label())  # 上部の余白用
        layout.add_widget(title_label)
        layout.add_widget(subtitle_label)

        # ボタンを中央に配置
        button = Button(text="実行", size_hint=(None, None), size=(150, 50))
        button.bind(on_press=self.show_confirmation_popup)

        center_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        center_layout.add_widget(Label())  # 左側の余白
        center_layout.add_widget(button)
        center_layout.add_widget(Label())  # 右側の余白
        layout.add_widget(center_layout)

        # ウィンドウサイズ変更時に背景の大きさを調整
        Window.bind(on_resize=self.on_window_resize)

        return layout

    def on_window_resize(self, instance, width, height):
        # ウィンドウサイズが変更されたときに呼ばれるメソッド
        self.set_background_color(self.background_color, width, height)

    def launch_main2(self, instance):
        # main2.pyを実行
        os.system("python MAINSYS/syokihaiti.py")

    def on_start(self):
        # CSVファイルから背景色を取得
        self.background_color, title_color, subtitle_color = self.get_colors_from_csv("MAINSYS/CSV/color_settings.csv")
        self.set_background_color(self.background_color, Window.width, Window.height)
        self.set_text_color(title_color, subtitle_color)

    def get_colors_from_csv(self, csv_file):
        background_color = (1, 1, 1)  # デフォルトの背景色（白）
        title_color = (0, 0, 0)  # デフォルトのタイトル文字色（黒）
        subtitle_color = (0, 0, 0)  # デフォルトのサブタイトル文字色（黒）

        with open(csv_file, "r") as file:
            reader = csv.reader(file)
            next(reader)  # ヘッダ行をスキップ
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

    def set_background_color(self, color, width, height):
        self.root.canvas.before.clear()  # 既存の背景をクリア
        with self.root.canvas.before:
            Color(*color)
            Rectangle(pos=self.root.pos, size=(width, height))

    def set_text_color(self, title_color, subtitle_color):
        # タイトルとサブタイトルの文字色を変更
        self.root.children[1].color = title_color  # タイトルの文字色を変更
        self.root.children[2].color = title_color  # サブタイトルの文字色を変更

    def show_confirmation_popup(self, instance):
        # ポップアップウィンドウを作成
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text='背景画像を選択しますか'))

        # はいボタン
        yes_button = Button(text='はい')
        yes_button.bind(on_press=self.launch_haikeigazou)

        # いいえボタン
        no_button = Button(text='いいえ')
        no_button.bind(on_press=self.dismiss_popup)
        
        content.add_widget(yes_button)
        content.add_widget(no_button)

        self.popup = Popup(title='確認', content=content, size_hint=(None, None), size=(300, 200))
        self.popup.open()

    def launch_haikeigazou(self, instance):
        # "haikeigazou.py" を実行
        os.system("python MAINSYS/haikeigazou.py")
        self.popup.dismiss()

    def dismiss_popup(self, instance):
        self.popup.dismiss()
        if instance.text == 'いいえ':
            # "syokihaiti.py" を実行
            os.system("python MAINSYS/teshaikei.py")

if __name__ == "__main__":
    MainApp().run()
