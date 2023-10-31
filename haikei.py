from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.colorpicker import ColorPicker
from kivy.graphics import Color, Rectangle
import csv
import japanize_kivy

class BackgroundChangerApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # ラベル
        label = Label(text="背景色を変更")

        # カラーピッカー
        self.color_picker = ColorPicker()
        self.color_picker.bind(color=self.on_color)

        # 画像ウィジェット
        self.background_image = Image(source='background.jpg')

        # ボタン
        button = Button(text="背景を変更")
        button.bind(on_release=self.change_background)

        # レイアウトにウィジェットを追加
        layout.add_widget(label)
        layout.add_widget(self.color_picker)
        layout.add_widget(self.background_image)
        layout.add_widget(button)

        return layout

    def on_color(self, instance, value):
        # カラーピッカーの色に背景色を変更
        self.background_image.canvas.before.clear()
        with self.background_image.canvas.before:
            Color(*value)
            Rectangle(pos=self.background_image.pos, size=self.background_image.size)

    def change_background(self, instance):
        # カラーピッカーの選択色をCSVファイルに保存
        selected_color = self.color_picker.color
        self.save_color_to_csv(selected_color)

        # 新しい背景画像を設定
        self.background_image.source = 'C:/Users/204004/Desktop/font/light-gray-concrete-wall.jpg'

    def save_color_to_csv(self, color):
        with open('color_settings.csv', 'w', newline='') as csvfile:
            fieldnames = ['Red', 'Green', 'Blue']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'Red': color[0], 'Green': color[1], 'Blue': color[2]})

if __name__ == '__main__':
    BackgroundChangerApp().run()