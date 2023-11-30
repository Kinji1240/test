from kivy.resources import resource_add_path
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.core.text import LabelBase
import time
import csv

class ClockScreen(Screen):
    def __init__(self, **kwargs):
        super(ClockScreen, self).__init__(**kwargs)

        self.layout = BoxLayout(orientation='vertical')

        self.clock_label = Label(text=self.get_japanese_time(), font_size='40sp', size_hint=(1, 0.7))
        self.layout.add_widget(self.clock_label)

        Clock.schedule_interval(self.update_time, 1)
        self.add_widget(self.layout)

        # 設定ファイルから情報を読み込む
        self.load_settings()

    def update_time(self, dt):
        self.clock_label.text = self.get_japanese_time()

    def get_japanese_time(self):
        current_time = time.strftime("%H:%M:%S", time.localtime())
        return current_time

    def load_settings(self):
        try:
            with open('settings.csv', 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    selected_font = row['font_name']
                    selected_color = [float(val) for val in row['selected_color'].split(',')]
                    self.apply_settings(selected_font, selected_color)
        except FileNotFoundError:
            pass

    def apply_settings(self, selected_font, selected_color):
        if selected_color:
            self.clock_label.color = selected_color
        if selected_font:
            if selected_font == 'NikkyouSans-mLKax.ttf':
                font_path = 'HoT_font/NikkyouSans-mLKax.ttf'  # パスの修正
                if LabelBase.have_font('NikkyouSans'):
                    LabelBase.unregister('NikkyouSans')
                LabelBase.register(name='NikkyouSans', fn_regular=font_path)
                self.clock_label.font_name = 'NikkyouSans'
            else:
                self.clock_label.font_name = selected_font

class TimeDisplayApp(App):
    def build(self):
        # フォントのパスを追加
        resource_add_path("HoT_font")

        self.sm = ScreenManager()

        clock_screen = ClockScreen(name='clock')
        self.sm.add_widget(clock_screen)

        return self.sm

if __name__ == '__main__':
    TimeDisplayApp().run()
