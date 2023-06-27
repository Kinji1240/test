from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button

class Screen1(Screen):
    pass

class Screen2(Screen):
    pass

# 必要なだけ画面を追加します

sm = ScreenManager()
sm.add_widget(Screen1(name='screen1'))
sm.add_widget(Screen2(name='screen2'))
# 他の画面も必要に応じて追加します

class Screen1(Screen):
    def __init__(self, **kwargs):
        super(Screen1, self).__init__(**kwargs)
        button = Button(text='Go to Screen 2')
        button.bind(on_release=self.switch_screen)
        self.add_widget(button)

    def switch_screen(self, *args):
        self.manager.current = 'screen2'

class MyApp(App):
    def build(self):
        return sm