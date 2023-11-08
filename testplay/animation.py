from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image

class MyKivyApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        # Screen1: 最初の画面
        screen1 = Screen(name="screen1")
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        with layout.canvas.before:
            self.background = Rectangle(source='C:/Users/204004/Desktop/font/cat.gif', pos=(0, 0), size=Window.size)

        font_name = 'C:/Users/204004/Desktop/font/NikkyouSans-mLKax.ttf'
        label = Label(text='Kivyサンプルアプリ', font_name=font_name, font_size=24)
        button = Button(text='別の画面に行く')
        button.bind(on_release=self.go_to_screen2)

        layout.add_widget(label)
        layout.add_widget(button)
        screen1.add_widget(layout)
        self.screen_manager.add_widget(screen1)

        # Screen2: 2番目の画面
        screen2 = Screen(name="screen2")
        layout2 = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        with layout2.canvas.before:
            self.background2 = Rectangle(source='C:/Users/204004/Desktop/font/another_background.png', pos=(0, 0), size=Window.size)

        label2 = Label(text='別の画面', font_name=font_name, font_size=24)
        back_button = Button(text='戻る')
        back_button.bind(on_release=self.go_to_screen1)

        layout2.add_widget(label2)
        layout2.add_widget(back_button)
        screen2.add_widget(layout2)
        self.screen_manager.add_widget(screen2)

        return self.screen_manager

    def go_to_screen2(self, instance):
        self.screen_manager.current = "screen2"

    def go_to_screen1(self, instance):
        self.screen_manager.current = "screen1"

if __name__ == '__main__':
    MyKivyApp().run()