from kivy.app import App
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.lang import Builder

#ウインドウの幅と高さの設定
Config.set('graphics', 'width', 600)
Config.set('graphics', 'height', 500)
#1でサイズ変更可、0はサイズ変更不可
Config.set('graphics', 'resizable', 1)
#kvファイルの読み込み
Builder.load_file("images.kv")

class MyLayout(Widget):
    def press1(self):
        self.ids.my_image.source = "photo1.jpg"

    def press2(self):
        self.ids.my_image.source = "photo2.jpg"

    def press3(self):
        self.ids.my_image.source = "photo3.jpg"

class DispimageApp(App):
    def build(self):
        self.title = "window"
        return MyLayout()

if __name__ == '__main__':
    DispimageApp().run()