from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Rectangle
from kivy.core.window import Window

class MyKivyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # 背景画像の設定
        with layout.canvas.before:
            background = Rectangle(source='C:/Users/204004/Desktop/font/light-gray-concrete-wall.jpg', pos=(0, 0), size=Window.size)

        # フォントファイルのパスを指定してフォントを使用
        font_name = 'C:/Users/204004/Desktop/font/NikkyouSans-mLKax.ttf'

        label = Label(text='Kivyサンプルアプリ', font_name=font_name, font_size=24)

        layout.add_widget(label)
        return layout

if __name__ == '__main__':
    MyKivyApp().run()


    #このコードでは、Rectangleのposを (0, 0) に設定し、sizeを Window.size に
    # 設定することで、背景画像をウィンドウの全画面に拡大表示しています。
    # Window.sizeは現在のウィンドウのサイズを表します。
    #これにより、背景画像がウィンドウ全体に表示されます。
    # ファイルパスが正しいことを確認し、ファイルが存在していることも
    # 確認してください。




