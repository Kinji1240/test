from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.metrics import cm
import japanize_kivy   

class MyKivyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # 背景画像の設定
        with layout.canvas.before:
            background = Rectangle(source='C:/Users/204004/Desktop/font/light-gray-concrete-wall.jpg', pos=(0, 0), size=Window.size)

        # フォントファイルのパスを指定してフォントを使用
        font_name = 'C:/Users/204004/Desktop/font/NikkyouSans-mLKax.ttf'

        label = Label(text='Kivyサンプルアプリ', font_name=font_name, font_size=24)

        # ボタンを作成し、レイアウトに追加
        button = Button(text='クリックしてください')
        
        # ボタンの大きさを縦3cm、横3cmに設定
        button.size_hint = (None, None)
        button.size = (cm(3), cm(3))
        
        layout.add_widget(label)
        layout.add_widget(button)
        
        return layout

if __name__ == '__main__':
    MyKivyApp().run()


