# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
import csv

class ColorDisplayApp(App):
    def build(self):
        # レイアウトの作成
        layout = BoxLayout(orientation='vertical')

        # CSVファイルから色情報を読み込む
        colors = self.load_colors_from_csv('test/settings.csv')

        # 色情報を表示
        for color in colors:
            label = Label(text=color['name'], size_hint_y=None, height=44)
            layout.add_widget(label)

            with label.canvas:
                Color(*color['rgb'])
                Rectangle(pos=label.pos, size=label.size)

        return layout

    def load_colors_from_csv(self, filename):
        colors = []
        try:
            with open(filename, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    color = {
                        'name': row['name'],
                        'rgb': [float(row['red']), float(row['green']), float(row['blue']), 1]
                    }
                    colors.append(color)
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        except Exception as e:
            print(f"Error reading CSV file: {e}")

        return colors

if __name__ == '__main__':
    ColorDisplayApp().run()
