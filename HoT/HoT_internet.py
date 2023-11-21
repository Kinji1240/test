from kivy.resources import resource_add_path
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
import time
import os
import csv
import japanize_kivy

class InternetScreen(Screen):
    def __init__(self, **kwargs):
        super(InternetScreen, self).__init__(**kwargs)

        self.layout = BoxLayout(orientation='vertical')

        # グレーの背景を描画
        with self.layout.canvas.before:
            Color(0.5, 0.5, 0.5, 1)  # グレーの色
            self.rect = Rectangle(size=self.layout.size, pos=self.layout.pos)

        # インターネット接続ステータスを表示するラベル
        self.status_label = Label(text='インターネットに接続しますか？', font_size='40sp', size_hint=(1, 0.5))
        self.layout.add_widget(self.status_label)

        # はい・いいえボタンを中央に配置するためのBoxLayout
        button_layout = BoxLayout(orientation='horizontal', size_hint=(0.5, 0.2), pos_hint={'center_x': 0.5, 'center_y': 0.6})
        self.layout.add_widget(button_layout)

        # はいボタン
        yes_button = Button(text='はい', size_hint=(0.5, 0.5), background_color=(1, 1, 1, 1))  # 白い背景
        yes_button.bind(on_press=self.connect_to_internet)
        button_layout.add_widget(yes_button)

        # いいえボタン
        no_button = Button(text='いいえ', size_hint=(0.5, 0.5), background_color=(1, 1, 1, 1))  # 白い背景
        no_button.bind(on_press=self.disconnect_from_internet)
        button_layout.add_widget(no_button)

        # 閉じるボタン
        close_button = Button(text='閉じる', size_hint=(0.2, 0.1), pos_hint={'top': 1, 'right': 1}, background_color=(1, 1, 1, 1))  # 白い背景
        close_button.bind(on_press=self.close_app)
        self.layout.add_widget(close_button)

        Clock.schedule_interval(self.update_status, 1)

        self.add_widget(self.layout)

    def update_status(self, dt):
        # インターネット接続ステータスの更新処理
        # (適切な実装が必要です)
        pass

    def connect_to_internet(self, instance):
        # インターネットに接続する処理
        # (適切な実装が必要です)
        pass

    def disconnect_from_internet(self, instance):
        # インターネットから切断する処理
        # (適切な実装が必要です)
        pass

    def close_app(self, instance):
        App.get_running_app().stop()

class TimeDisplayApp(App):
    def build(self):
        # フォントのパスを追加
        resource_add_path(os.path.abspath("HoT_font"))

        self.sm = ScreenManager()

        internet_screen = InternetScreen(name='internet')  # インターネット画面を追加

        self.sm.add_widget(internet_screen)

        return self.sm

if __name__ == '__main__':
    TimeDisplayApp().run()
