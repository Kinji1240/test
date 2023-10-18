from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.core.text import LabelBase, DEFAULT_FONT  # 追加分
from kivy.resources import resource_add_path  # 追加分

resource_add_path('font')  # 追加分
LabelBase.register(DEFAULT_FONT, 'NikkyouSans-mLKax.ttf')  # 追加分
 
# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
 
#Builder.load_file("sm01.kv")

# Declare both screens
class MenuScreen(Screen):
    pass
 
class SettingsScreen(Screen):
    pass
 
class SM01App(App):
 
    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))
 
        return sm
 
if __name__ == '__main__':
    SM01App().run()