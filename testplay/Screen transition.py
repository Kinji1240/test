from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

import japanize_kivy            # [パターン１] 日本語表示させる japanize_kivy
                                #              モジュールを import する
                                #             (この１行のみで可能)
                                #             (日本語フォント：IPAexゴシックで表示される)

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        label = Label(text="ホーム画面")
        button = Button(text="次へ", on_release=self.go_to_second_screen)
        layout.add_widget(label)
        layout.add_widget(button)
        self.add_widget(layout)

    def go_to_second_screen(self, instance):
        app.screen_manager.current = "second"

class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        label = Label(text="セカンド画面")
        button = Button(text="戻る", on_release=self.go_to_home_screen)
        layout.add_widget(label)
        layout.add_widget(button)
        self.add_widget(layout)

    def go_to_home_screen(self, instance):
        app.screen_manager.current = "home"

class MyApp(App):
    def build(self):
        # Screen Managerを作成
        self.screen_manager = ScreenManager()

        # ホーム画面を追加
        home_screen = HomeScreen(name="home")
        self.screen_manager.add_widget(home_screen)

        # セカンド画面を追加
        second_screen = SecondScreen(name="second")
        self.screen_manager.add_widget(second_screen)

        return self.screen_manager

if __name__ == '__main__':
    app = MyApp()
    app.run()