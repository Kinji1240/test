from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics import Rectangle

class MyKivyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # 背景画像の設定
        with layout.canvas.before:
            background = Rectangle(source='C:/Users/204004/Desktop/font/light-gray-concrete-wall.jpg', pos=layout.pos, size=layout.size)

        # フォントファイルのパスを指定してフォントを使用
        font_name = 'C:/Users/204004/Desktop/font/NikkyouSans-mLKax.ttf'

        label = Label(text='Kivyサンプルアプリ', font_name=font_name, font_size=24)

        layout.add_widget(label)
        return layout

if __name__ == '__main__':
    MyKivyApp().run()