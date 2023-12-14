from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.colorpicker import ColorPicker
import csv
import os
from kivy.core.window import Window
import japanize_kivy
import subprocess
import time

class BackgroundChangerApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # ラベル（文字色変更用）
        label_text = Label(text="文字色変更")
        self.label_text = label_text

        # カラーピッカー（文字色用）
        self.text_color_picker = ColorPicker()
        self.text_color_picker.bind(color=self.on_text_color)

        # ボタン
        button = Button(text="文字色を変更", on_press=self.change_text_color)

        # レイアウトにウィジェットを追加
        layout.add_widget(label_text)
        layout.add_widget(self.text_color_picker)
        layout.add_widget(button)

        # ウィンドウサイズ変更時にオブジェクトを調整
        Window.bind(on_resize=self.on_window_resize)

        # optファイルから文字色情報をロード
        text_red, text_green, text_blue, text_alpha = self.loadopt()

        # 初期文字色を設定
        self.label_text.color = (text_red, text_green, text_blue, text_alpha)

        return layout

    def on_window_resize(self, instance, width, height):
        # ウィンドウサイズが変更されたときに呼ばれるメソッド
        # フォントサイズを調整
        font_size = int(0.04 * height)  # 画面高さの4%をフォントサイズとする
        self.label_text.font_size = font_size

    def on_text_color(self, instance, value):
        # ラベルの文字色を変更
        self.label_text.color = value

    def change_text_color(self, instance):
        # カラーピッカーの選択色をCSVファイルに保存
        text_color = self.text_color_picker.color

        # 文字色のRGBA値を取得
        text_red, text_green, text_blue, text_alpha = text_color

        # csvファイルの保存先ディレクトリ
        csv_dir = 'MAINSYS/CSV'

        # ディレクトリが存在しない場合、作成
        if not os.path.exists(csv_dir):
            os.makedirs(csv_dir)

        # csvファイルの保存パス
        csv_path = os.path.join(csv_dir, 'onoD_opt.csv')

        # 既存のonoD_opt.csvの内容を読み取り
        opt_data = self.read_opt_csv(csv_path)

        # リストのサイズが足りない場合、エラーを表示
        if len(opt_data) < 8:
            print("エラー: CSVファイルに十分な行がありません。")
            return

        # 8行目の情報が足りない場合、エラーを表示
        if len(opt_data[7]) < 2:
            print("エラー: 8行目に十分な列がありません。")
            return

        # 8行目の情報を更新
        opt_data[7][1] = f"{text_red},{text_green},{text_blue},{text_alpha}"

        # 更新されたデータをcsvファイルに保存
        self.save_opt_csv(csv_path, opt_data)

        # 保存後に別のPythonスクリプトを実行
        script_path = 'MAINSYS/PROGRAMS/pos_mover.py'
        if os.path.exists(script_path):
            subprocess.Popen(["python", script_path])
            App.get_running_app().stop()
        else:
            print(f"スクリプト '{script_path}' は存在しません。")

    def read_opt_csv(self, csv_file):
        data = []
        if os.path.exists(csv_file):
            with open(csv_file, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    data.append(row)
        return data

    def save_opt_csv(self, csv_file, data):
        with open(csv_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)

    def loadopt(self):
        # CSVファイルに保存された文字色情報を読み込むメソッド
        filename = 'MAINSYS/CSV/onoD_opt.csv'
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)

            # 文字色情報を取得
            font_color_data = data[7][1]

            if font_color_data:
                # もし font_color_data が空文字列でなければ、RGBAの各値を取得
                text_red, text_green, text_blue, text_alpha = map(float, font_color_data.split(','))
            else:
                # 空文字列の場合はデフォルト値を設定
                text_red, text_green, text_blue, text_alpha = 1.0, 1.0, 1.0, 1.0

        

        return text_red, text_green, text_blue, text_alpha, 


if __name__ == '__main__':
    BackgroundChangerApp().run()
