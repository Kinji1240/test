import pandas as pd
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.core.window import Window
import csv
import requests
import japanize_kivy
from datetime import datetime

class WeatherApp(App):

    def build(self):
        layout = BoxLayout(orientation='vertical')
        coordinates_df = pd.read_csv('test/LYtest/47都道府県IDOKEIDO-UTF8.csv')

        if 'latitude' in coordinates_df.columns and 'longitude' in coordinates_df.columns:
            self.selected_data = None
            spinner_values = coordinates_df['都道府県'].tolist()
            spinner = Spinner(text='都道府県を選択', values=spinner_values)
            

            def on_spinner_change(spinner, text):
                self.selected_data = coordinates_df[coordinates_df['都道府県'] == text].iloc[0]

            spinner.bind(text=on_spinner_change)
            layout.add_widget(spinner)

            # 日数を選択する Spinner を追加
            days_spinner = Spinner(text='日数を選択', values=['1日', '3日'])
            layout.add_widget(days_spinner)

            # BoxLayout を追加して横に並べる
            horizontal_layout = BoxLayout(orientation='vertical')
            layout.add_widget(horizontal_layout)

            def saveopt(tiikidata, daydata):
            # CSVファイルからボタンの座標を取得するメソッド
                filename = 'test\onoD\onoD_csv_list\onoD_opt.csv'
                with open(filename, 'r') as csvfile:
                    reader = csv.reader(csvfile)
                    data = list(reader)
                    
                    data[3][1] = tiikidata
                    data[4][1] = daydata

                # ここで CSV ファイルに書き込む
                with open(filename, 'w', newline='') as csvfile:
                    csv_writer = csv.writer(csvfile)
                    csv_writer.writerows(data)

            def re_setting(instance):
                print(spinner)
                return

            update_button = Button(text="地域を保存", size_hint=(None, None))
            update_button.bind(on_press=lambda instance: saveopt(tiikidata=self.selected_data, daydata=days_spinner.text))
            layout.add_widget(update_button)

            re_button = Button(text="戻る", size_hint=(None, None))
            re_button.bind(on_press=re_setting)
            layout.add_widget(re_button)

            return layout
        else:
            return Label(text="エラー: CSVファイルに 'latitude' と 'longitude' の列がありません。")

if __name__ == '__main__':
    WeatherApp().run()
