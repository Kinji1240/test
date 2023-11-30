from kivy.resources import resource_add_path
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.core.text import LabelBase
import time
import os
import csv
from kivy.properties import StringProperty, ListProperty
import japanize_kivy

class ClockScreen(Screen):
    selected_color = ListProperty([1, 1, 1, 1])
    selected_font = StringProperty('')

    def __init__(self, **kwargs):
        super(ClockScreen, self).__init__(**kwargs)

        self.layout = BoxLayout(orientation='vertical')

        self.clock_label = Label(text=self.get_japanese_time(), font_size='40sp', size_hint=(1, 0.7))
        self.layout.add_widget(self.clock_label)

        Clock.schedule_interval(self.update_time, 1)  # 1秒ごとに時間を更新
        self.add_widget(self.layout)
        self.selected_color = [1, 1, 1, 1]
        self.selected_font = ''  # 空の文字列で初期化

    def update_time(self, dt):
        self.clock_label.text = self.get_japanese_time()
        # 新しく追加した部分: 色情報とフォント情報を使用してラベルのスタイルを更新
        if self.selected_color:
            self.clock_label.color = self.selected_color
        if self.selected_font:
            self.clock_label.font_name = self.selected_font

    def get_japanese_time(self):
        current_time = time.strftime("%H:%M:%S", time.localtime())
        return current_time

class ClockApp(App):
    def build(self):
        # フォントのパスを追加
        resource_add_path(os.path.abspath("HoT_font"))

        # ScreenManagerを作成
        self.sm = ScreenManager()

        # ClockScreenを作成し、ScreenManagerに追加
        clock_screen = ClockScreen(name='clock')
        self.sm.add_widget(clock_screen)

        # アプリを起動
        return self.sm

    def on_start(self):
        # アプリが起動したときに実行されるメソッド
        self.load_settings()

    def load_settings(self):
        try:
            # settings.csvから情報を読み込んで時計の設定を更新
            with open('settings.csv', 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    selected_font = row['font_name']
                    selected_color = [float(val) for val in row['selected_color'].split(',')]

                    # ScreenManagerからClockScreenを取得し、設定を更新
                    clock_screen = self.sm.get_screen('clock')
                    clock_screen.selected_font = selected_font
                    clock_screen.selected_color = selected_color
        except FileNotFoundError:
            pass

# アプリを起動
if __name__ == '__main__':
    ClockApp().run()
