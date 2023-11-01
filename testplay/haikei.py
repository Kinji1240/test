from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.colorpicker import ColorPicker
from kivy.graphics import Color, Rectangle
import japanize_kivy

class BackgroundChangerApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # ラベル
        self.label = Label(text="背景色と文字色を変更")

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
        button.bind(on_release=self.change_background)

        # レイアウトにウィジェットを追加
        layout.add_widget(self.label)
        layout.add_widget(self.background_color_picker)
        layout.add_widget(self.text_color_picker)
        layout.add_widget(self.background_image)
        layout.add_widget(button)

        return layout

    def on_background_color(self, instance, value):
        self.background_image.canvas.before.clear()
        with self.background_image.canvas.before:
            Color(*value)
            Rectangle(pos=self.background_image.pos, size=self.background_image.size)

    def on_text_color(self, instance, value):
        self.label.color = value

    def change_background(self, instance):
        # 画像を変更
        self.background_image.source = 'C:/Users/204004/Desktop/font/light-gray-concrete-wall.jpg'

if __name__ == '__main__':
    BackgroundChangerApp().run()