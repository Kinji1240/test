from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import japanize_kivy
import csv

# CSVファイルのパス
csv_filename = "font_info.csv"

# 二行目のデータを文字列として取得
second_row_data = ""
try:
    with open(csv_filename, 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # 一行目を読み飛ばす
        second_row = next(csv_reader, None)  # 二行目を取得
        if second_row:
            second_row_data = second_row[0]  # 二行目のデータ（最初の列）を取得
except FileNotFoundError:
    print("CSVファイルが見つかりません。")

# second_row_dataにCSVファイルの二行目のデータが文字列として格納されています
if second_row_data:
    print("CSVファイルの二行目のデータ:")
    print(second_row_data)

class MyKivyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # フォントファイルのパスを指定してフォントを使用石川のデスクトップにあるから無理
        font_name = second_row_data
        
        label = Label(text='Kivyサンプルアプリ', font_name=font_name, font_size=24)
        
        layout.add_widget(label)
        return layout

if __name__ == '__main__':
    MyKivyApp().run()