from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
import japanize_kivy

class Screen1(Screen):
    def __init__(self, **kwargs):
        super(Screen1, self).__init__(**kwargs)
        self.add_widget(Button(text="Go to Screen 2", on_press=self.change_screen))

    def change_screen(self, instance):
        app = App.get_running_app()
        app.screen_manager.current = 'screen2'

class Screen2(Screen):
    def __init__(self, **kwargs):
        super(Screen2, self).__init__(**kwargs)
        self.add_widget(Button(text="Go to Screen 1", on_press=self.change_screen))

    def change_screen(self, instance):
        app = App.get_running_app()
        app.screen_manager.current = 'screen1'

class MyApp(App):
    def build(self):
        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(Screen1(name='screen1'))
        self.screen_manager.add_widget(Screen2(name='screen2'))
        return self.screen_manager
