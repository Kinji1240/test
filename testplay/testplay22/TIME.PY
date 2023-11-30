from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserIconView
from kivy.core.text import LabelBase
from kivy.clock import Clock
from datetime import datetime
import os
import csv
import pandas as pd

class DigitalClock(BoxLayout):
    def __init__(self, **kwargs):
        super(DigitalClock, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # デジタル時計の表示用ラベル
        self.time_label = Label(text=self.get_time(), font_size='50sp')
        self.add_widget(self.time_label)

        # ColorPickerウィジェット
        self.color_picker = ColorPicker()
        self.color_picker.bind(color=self.on_color_picker_change)
        self.add_widget(self.color_picker)

        # フォント選択ボタン
        font_button = Button(text='Select Font', on_press=self.show_font_selector)
        self.add_widget(font_button)

        # フォントの相対パスと初期値
        self.font_path = self.get_latest_font_from_csv()  # 最新のフォント情報を取得
        self.set_font(self.font_path)

        # 時刻を更新する関数を1秒ごとにスケジュール
        Clock.schedule_interval(self.update_time, 1)

        # Popup ウィジェットを DigitalClock クラスの一部として保持
        self.popup = Popup(title='Select Font', size_hint=(0.9, 0.9))

    def get_latest_font_from_csv(self):
        # CSVファイルから最新のフォント情報を取得
        try:
            df = pd.read_csv("CSV/selected_fonts.csv")
            if not df.empty:
                # 最後の行のフォント情報を取得
                latest_font_path = df.iloc[-1]['SelectedFont']
                return latest_font_path
        except FileNotFoundError:
            print("CSV file not found.")
        except Exception as e:
            print(f"Error reading CSV file: {e}")

        # ファイルが見つからないかエラーが発生した場合はデフォルトのフォントを返す
        return "font/Mystic_Soul.ttf"

    def get_time(self):
        # 現在の時刻を取得
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return current_time

    def update_time(self, dt):
        # 時刻を更新
        self.time_label.text = self.get_time()

    def on_color_picker_change(self, instance, value):
        # ColorPickerの色が変更されたときに呼び出されるコールバック関数
        self.time_label.color = value

    def set_font(self, font_path):
        # フォントを設定
        LabelBase.register(name="DigitalClockFont", fn_regular=font_path)
        self.time_label.font_name = "DigitalClockFont"

    def show_font_selector(self, instance):
        # フォント選択ダイアログを表示する
        file_chooser = FileChooserIconView()
        file_chooser.path = os.path.abspath("font")  # フォントが格納されているディレクトリを指定

        file_chooser.bind(on_submit=self.select_font)
        file_chooser.bind(on_cancel=self.popup.dismiss)

        # Popup ウィジェットに content を設定
        self.popup.content = file_chooser

        # Popup ウィジェットを表示
        self.popup.open()

    def select_font(self, instance, selection, touch):
        # フォントが選択されたときの処理
        if selection:
            font_path = os.path.join(instance.path, selection[0])
            self.set_font(font_path)
            # CSVに選択されたフォント情報を上書き保存
            self.write_to_csv(font_path)
        # Popup ウィジェットを閉じる
        self.popup.dismiss()

    def write_to_csv(self, font_path):
        # CSVファイルを読み込んでDataFrameに変換
        try:
            df = pd.read_csv("CSV/selected_fonts.csv")
        except FileNotFoundError:
            print("CSV file not found.")
            return
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            return

        # DataFrameの最後の行を新しいデータで上書き
        df.iloc[-1] = [datetime.now().strftime("%Y-%m-%d %H:%M:%S"), font_path]

        # DataFrameをCSVファイルに保存
        df.to_csv("CSV/selected_fonts.csv", index=False)

class DigitalClockApp(App):
    def build(self):
        return DigitalClock()

if __name__ == '__main__':
    DigitalClockApp().run()
