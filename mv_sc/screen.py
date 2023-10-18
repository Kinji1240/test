from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout


class MainMenu(BoxLayout):
    pass


class SubMenu(BoxLayout):
    pass


class MainScreen(Screen):
    pass


class SubScreen(Screen):
    pass


class ScreenApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(MainScreen(name='main'))
        self.sm.add_widget(SubScreen(name='sub'))
        return self.sm


if __name__ == '__main__':
    ScreenApp().run()