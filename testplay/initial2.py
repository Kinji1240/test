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

        # ルートレイアウト
        root_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # タイトルラベル
        title_label = Label(text="ほしい機能を選んでね", size_hint=(1, None), height=50, halign='center', valign='middle')
        root_layout.add_widget(title_label)

        # 時間表示ボタン
        time_button = Button(text="時間表示", on_release=self.go_to_second_screen)
        root_layout.add_widget(time_button)

        # 天気の時間表示ボタン
        weather_button = Button(text="天気表示", on_release=self.go_to_serd_screen)
        root_layout.add_widget(weather_button)

        # 予定の時間表示ボタン
        schedule_button = Button(text="予定表示", on_release=self.go_to_serd_screen)
        root_layout.add_widget(schedule_button)

        # +の時間表示ボタン
        plus_button = Button(text="+", on_release=self.go_to_serd_screen)
        root_layout.add_widget(plus_button)

        # 背景の時間表示ボタン
        background_button = Button(text="背景", on_release=self.go_to_serd_screen)
        root_layout.add_widget(background_button)

        # 確定ボタン
        confirm_button = Button(text="確定", on_release=self.go_to_serd_screen)
        root_layout.add_widget(confirm_button)

        # レイアウトを画面に追加
        self.add_widget(root_layout)

    def go_to_second_screen(self, instance):
        app.screen_manager.current = "second"

    
    def go_to_serd_screen(self, instance):
        app.screen_manager.current = "serd"



class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        button = Button(text="次へ", on_release=self.go_to_home_screen)
        layout.add_widget(button)
        self.add_widget(layout)

    def go_to_home_screen(self, instance):
        app.screen_manager.current = "serd"

class SerdScreen(Screen):
    def __init__(self, **kwargs):
        super(SerdScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        button = Button(text="戻る", on_release=self.go_to_serd_screen)
        layout.add_widget(button)
        self.add_widget(layout)

    def go_to_serd_screen(self, instance):
        app.screen_manager.current = "home"
    
        
    '''def go_to_second_screen(self, instance):
        app.screen_manager.current = "second"

        # ボタンを作成し、レイアウトに追加
        
        weather_button = Button(text="天気表示")
        schedule_button = Button(text="予定表示")
        plus_button = Button(text="+")
        background_button = Button(text="背景")
        
        # 確定ボタン
        confirm_button = Button(text="確定", size_hint=(None, None), height=50)

        # ウィジェットをレイアウトに追加
        root_layout.add_widget(title_label)
        button_layout = BoxLayout(spacing=10)
        button_layout.add_widget(time_button)
        button_layout.add_widget(weather_button)
        button_layout.add_widget(schedule_button)
        button_layout.add_widget(plus_button)
        button_layout.add_widget(background_button)
        root_layout.add_widget(button_layout)
        root_layout.add_widget(confirm_button)

        return root_layout'''
    
class MyApp(App):
    def build(self):
        self.screen_manager = ScreenManager()
        home_screen = HomeScreen(name="home")
        self.screen_manager.add_widget(home_screen)
        second_screen = SecondScreen(name="second")
        self.screen_manager.add_widget(second_screen)
        serd_screen = SerdScreen(name="serd")
        self.screen_manager.add_widget(serd_screen)
        return self.screen_manager
    
if __name__ == '__main__':
    app = MyApp()
    #app = FeatureSelectionApp()
    app.run()
