from kivy.app import App
from kivy.config import Config

from kivy.uix.widget import Widget
from kivy.lang import Builder
import japanize_kivy

#ウインドウの幅と高さの設定
Config.set('graphics', 'width', 600)
Config.set('graphics', 'height', 500)
#1でサイズ変更可、0はサイズ変更不可
Config.set('graphics', 'resizable', 1)

from kivy.core.text import LabelBase, DEFAULT_FONT  # 追加分
from kivy.resources import resource_add_path  # 追加分


#kvファイルの読み込み
Builder.load_file("mylayout.kv")

class MyLayout(Widget):
    def press1(self):
        self.ids.my_image.source = "image/f3978ebc-9030-49e7-aa5e-4a370a955e1b.jpg"

    def press2(self):
        self.ids.my_image.source = "image/fc3daa7234c7326abcef144075ce62649d3b1113.jpg"

    def press3(self):
        self.ids.my_image.source = "image/0cd456a4-71c5-46f3-9bea-4ccf155c7a89.jpg"

    def press4(self):
        self.ids.manager.current = "goto01.txt"


class DispimageApp(App):
    def build(self):
        self.title = "window"
        return MyLayout()

if __name__ == '__main__':
    DispimageApp().run()
