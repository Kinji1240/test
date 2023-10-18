from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.image import Image
from PIL import Image as PILImage

class MyKivyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # 背景画像の設定
        with layout.canvas.before:
            self.background = Rectangle(source='C:/Users/204004/Desktop/font/cat.gif', pos=(0, 0), size=Window.size)

        # フォントファイルのパスを指定してフォントを使用
        font_name = 'C:/Users/204004/Desktop/font/NikkyouSans-mLKax.ttf'

        label = Label(text='Kivyサンプルアプリ', font_name=font_name, font_size=24)

        layout.add_widget(label)
        
        # アニメーションの開始
        Clock.schedule_interval(self.scroll_background, 1/30.0)  # 30 FPSで更新

        return layout

    def scroll_background(self, dt):
        # 背景をスクロール
        self.background.pos = (self.background.pos[0] - 2, self.background.pos[1])

        if self.background.pos[0] < -self.background.size[0]:
            self.background.pos = (Window.width, self.background.pos[1])

if __name__ == '__main__':
    MyKivyApp().run()