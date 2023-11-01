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
        label = Label(text="背景色と文字色を変更")
        self.label = label  # ラベルを属性として保存

        # カラーピッカー（背景色用）
        self.background_color_picker = ColorPicker()
        self.background_color_picker.bind(color=self.on_background_color)

        # カラーピッカー（文字色用）
        self.text_color_picker = ColorPicker()
        self.text_color_picker.bind(color=self.on_text_color)

        # 画像ウィジェット
        self.background_image = Image(source='background.jpg')

        # ボタン
        button = Button(text="背景と文字色を変更")
        button.bind(on_release=self.change_background_and_text_color)

        # レイアウトにウィジェットを追加
        layout.add_widget(label)
        layout.add_widget(self.background_color_picker)
        layout.add_widget(self.text_color_picker)
        layout.add_widget(self.background_image)
        layout.add_widget(button)

        return layout

    def on_background_color(self, instance, value):
        # カラーピッカーの色に背景色を変更
        self.background_image.canvas.before.clear()
        with self.background_image.canvas.before:
            Color(*value)
            Rectangle(pos=self.background_image.pos, size=self.background_image.size)

    def on_text_color(self, instance, value):
        # ラベルの文字色を変更
        self.label.color = value

    def change_background_and_text_color(self, instance):
        # カラーピッカーの選択色をCSVファイルに保存
        background_color = self.background_color_picker.color
        text_color = self.text_color_picker.color

        self.save_colors_to_csv(background_color, text_color)

        # 新しい背景画像を設定
        self.background_image.source = 'MAINSYS/FONT/light-gray-concrete-wall.jpg'

    def save_colors_to_csv(self, background_color, text_color):
        with open('color_settings.csv', 'w', newline='') as csvfile:
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
if __name__ == '__main__':
    BackgroundChangerApp().run()