from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

import japanize_kivy            # [パターン１] 日本語表示させる japanize_kivy
                                #              モジュールを import する
                                #             (この１行のみで可能)
                                #             (日本語フォント：IPAexゴシックで表示される)


class FeatureSelectionApp(App):
    def build(self):
        # ルートレイアウト
        root_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # タイトルラベル
        title_label = Button(text="ほしい機能を選んでね", size_hint=(1, None), height=50, disabled=True, halign='center', valign='middle')

        # ボタンを作成し、レイアウトに追加
        time_button = Button(text="時間表示")
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

        return root_layout

if __name__ == '__main__':
    app = FeatureSelectionApp()
    app.run()