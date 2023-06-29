# フル画面を解除して画面の幅と高さを設定
from kivy.config import Config
Config.set('graphics', 'fullscreen', 0)
Config.set('graphics', 'width', 320)
Config.set('graphics', 'height', 568)
Config.set('graphics', 'resizable', 0)

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

from kivy.core.text import LabelBase, DEFAULT_FONT  # 追加分
from kivy.resources import resource_add_path  # 追加分

resource_add_path('c:/Windows/Fonts')  # 追加分
LabelBase.register(DEFAULT_FONT, 'NikkyouSans-mLKax.ttf')  # 追加分

class MainScreen(BoxLayout):
    pass

class TestApp(App):
    def build(self):
        self.title = 'テスト'
        return MainScreen()

if __name__ == '__main__':
    TestApp().run()