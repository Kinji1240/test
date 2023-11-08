from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
 
from kivy.config import Config
 
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '480')

from kivy.core.text import LabelBase, DEFAULT_FONT  # 追加分
from kivy.resources import resource_add_path  # 追加分

resource_add_path('font')  # 追加分
LabelBase.register(DEFAULT_FONT, 'NikkyouSans-mLKax.ttf')  # 追加分
 
class Display(BoxLayout):
    pass
 
class Screen_One(Screen):
    pass
 
class Screen_Two(Screen):
    pass
 
class SM02App(App):
    def build(self):
        return Display()
 
if __name__ == '__main__':
    SM02App().run()