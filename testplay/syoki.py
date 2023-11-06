import csv
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.image import Image
from kivy.core.window import Window
import japanize_kivy

class BackgroundChangerApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # ラベル（背景色変更用）
        label_background = Label(text="背景色変更")
        self.label_background = label_background

        # カラーピッカー（背景色用）
        self.background_color_picker = ColorPicker()
        self.background_color_picker.bind(color=self.on_background_color)

        # ラベル（文字色変更用）
        label_text = Label(text="文字色変更")
        self.label_text = label_text

        # カラーピッカー（文字色用）
        self.text_color_picker = ColorPicker()
        self.text_color_picker.bind(color=self.on_text_color)

        # ボタン
        button = Button(text="背景色と文字色を変更", on_press=self.change_background_and_text_color)

        # レイアウトにウィジェットを追加
        layout.add_widget(label_background)
        layout.add_widget(self.background_color_picker)
        layout.add_widget(label_text)
        layout.add_widget(self.text_color_picker)
        layout.add_widget(button)

        # ウィンドウサイズ変更時にオブジェクトを調整
        Window.bind(on_resize=self.on_window_resize)

        return layout

    def on_window_resize(self, instance, width, height):
        # ウィンドウサイズが変更されたときに呼ばれるメソッド
        # フォントサイズを調整
        font_size = int(0.04 * height)  # 画面高さの4%をフォントサイズとする
        self.label_background.font_size = font_size
        self.label_text.font_size = font_size

    def on_background_color(self, instance, value):
        # カラーピッカーの色に背景色を変更
        # バックグラウンド画像を含む場合に使用
        pass

    def on_text_color(self, instance, value):
        # ラベルの文字色を変更
        self.label_background.color = value
        self.label_text.color = value

    def change_background_and_text_color(self, instance):
        # カラーピッカーの選択色をCSVファイルに保存
        background_color = self.background_color_picker.color
        text_color = self.text_color_picker.color

        # CSVファイルに背景色を保存
        self.save_colors_to_csv(background_color, text_color)

        # 新しい背景画像を設定
        self.set_background_image(background_color)

    def save_colors_to_csv(self, background_color, text_color):
        # csvファイルの保存先ディレクトリ
        csv_dir = 'MAINSYS/CSV'

        # ディレクトリが存在しない場合、作成
        if not os.path.exists(csv_dir):
            os.makedirs(csv_dir)

        # csvファイルの保存パス
        csv_path = os.path.join(csv_dir, 'color_settings.csv')

        with open(csv_path, 'w', newline='') as csvfile:
            fieldnames = ['BackgroundRed', 'BackgroundGreen', 'BackgroundBlue', 'TextRed', 'TextGreen', 'TextBlue']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({
                'BackgroundRed': background_color[0],
                'BackgroundGreen': background_color[1],
                'BackgroundBlue': background_color[2],
                'TextRed': text_color[0],
                'TextGreen': text_color[1],
                'TextBlue': text_color[2]
            })

    def set_background_image(self, background_color):
        # 背景画像を設定
        csv_dir = 'MAINSYS/CSV'
        csv_path = os.path.join(csv_dir, 'color_settings.csv')

        with open(csv_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            row = next(reader)  # 一番最初の行を読み取る
            background_red = float(row['BackgroundRed'])
            background_green = float(row['BackgroundGreen'])
            background_blue = float(row['BackgroundBlue'])

        # 背景色に基づいて背景画像を生成
        background_image = Image(source='', keep_ratio=False, allow_stretch=True)
        background_image.canvas.before.clear()
        with background_image.canvas.before:
            Color(background_red, background_green, background_blue, 1)
            Rectangle(pos=background_image.pos, size=background_image.size)
        self.root.add_widget(background_image)

if __name__ == '__main__':
    BackgroundChangerApp().run()