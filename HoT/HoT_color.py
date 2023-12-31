from kivy.resources import resource_add_path
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.dropdown import DropDown
from kivy.clock import Clock
from kivy.core.text import LabelBase
import time
import os
import csv
from kivy.properties import StringProperty, ListProperty

class FontSettingScreen(Screen):
    selected_font = StringProperty('')
    selected_color = ListProperty([1, 1, 1, 1])

    def __init__(self, **kwargs):
        super(FontSettingScreen, self).__init__(**kwargs)
        # アプリ起動時に保存された情報を読み込んで適用
        self.load_settings_once()

        self.layout = BoxLayout(orientation='vertical')

        back_button = Button(text='戻る', size_hint=(0.1, 0.1))
        back_button.bind(on_press=self.back_action)
        self.layout.add_widget(back_button)

        self.font_label = Label(text='フォント設定画面', font_size='40sp', size_hint=(1, 0.7))
        self.layout.add_widget(self.font_label)

        # フォント選択用のドロップダウンメニューを作成
        self.font_dropdown = DropDown()
        font_options = ['Arial', 'Verdana', 'NikkyouSans-mLKax.ttf']
        for font_option in font_options:
            btn = Button(text=font_option, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.change_font(btn.text))
            self.font_dropdown.add_widget(btn)

        font_button = Button(text='フォント選択', size_hint=(0.2, 0.1))
        font_button.bind(on_release=self.font_dropdown.open)
        self.layout.add_widget(font_button)

        self.font_dropdown.bind(on_select=lambda instance, x: setattr(font_button, 'text', x))

        # 確定ボタン
        confirm_button = Button(text='確定', size_hint=(1, 0.1))
        confirm_button.bind(on_press=self.confirm_action)
        self.layout.add_widget(confirm_button)

        Clock.schedule_interval(self.update_time, 1)
        self.add_widget(self.layout)

    def on_leave(self):
        # 画面を離れるときに設定を保存
        self.save_settings()

    def load_settings_once(self):
        if not hasattr(self, 'settings_loaded'):
            self.load_settings()
            self.settings_loaded = True

    def load_settings(self):
        try:
            with open('settings.csv', 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    self.selected_font = row['font_name']
                    self.selected_color = [float(val) for val in row['selected_color'].split(',')]
                    self.apply_settings()  # 保存された情報を適用
        except FileNotFoundError:
            pass

    def save_settings(self):
        with open('settings.csv', 'w', newline='') as csvfile:
            fieldnames = ['font_name', 'selected_color']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            for row in [{'font_name': self.selected_font, 'selected_color': ','.join(map(str, self.selected_color))}]:
                writer.writerow(row)

    def update_time(self, dt):
        self.font_label.text = self.get_japanese_time()
        # 新しく追加した部分: 色情報とフォント情報を使用してフォントラベルのスタイルを更新
        if self.selected_color:
            self.font_label.color = self.selected_color

    def get_japanese_time(self):
        current_time = time.strftime("%H:%M:%S", time.localtime())
        return current_time

    def back_action(self, instance):
        print("戻るボタンが押されました。")
        self.manager.current = 'main'

    def change_font(self, font_name):
        if font_name == 'NikkyouSans-mLKax.ttf':
            # ここにフォントファイルの絶対パスを挿入
            font_path = r'HoT_font\NikkyouSans-mLKax.ttf'
            if os.path.exists(font_path):
                LabelBase.register(name='NikkyouSans', fn_regular=font_path)
                self.font_label.font_name = 'NikkyouSans'
                # 新しく追加した部分: フォント情報を格納
                self.selected_font = 'NikkyouSans'
        else:
            # 新しく追加した部分: フォント情報を格納
            self.font_label.font_name = font_name
            self.selected_font = font_name

    def confirm_action(self, instance):
        print("確定ボタンが押されました。")
        clock_screen = self.manager.get_screen('clock')
        clock_screen.selected_color = self.selected_color
        clock_screen.selected_font = self.selected_font
        self.manager.current = 'clock'


class MainScreen(Screen):
    selected_color = ListProperty([1, 1, 1, 1])

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        self.layout = BoxLayout(orientation='vertical')

        self.time_label = Label(text=self.get_japanese_time(), font_size='40sp', size_hint=(1, 0.7))
        self.layout.add_widget(self.time_label)

        # 色の選択ボタンを追加
        color_buttons = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        colors = [(1, 0, 0, 1), (0, 1, 0, 1), (0, 0, 1, 1), (1, 1, 0, 1), (1, 0, 1, 1), (0, 1, 1, 1), (0.5, 0.5, 0.5, 1), (1, 1, 1, 1)]
        for color in colors:
            color_button = Button(background_color=color, size_hint=(0.125, 1))
            color_button.bind(on_press=lambda instance, color=color: self.change_color(color))
            color_buttons.add_widget(color_button)

        self.layout.add_widget(color_buttons)

        # 確定ボタン
        confirm_button = Button(text='確定', size_hint=(1, 0.1))
        confirm_button.bind(on_press=lambda instance: self.confirm_action(self.time_label.color))
        confirm_button.bind(on_press=self.switch_to_font_setting)
        self.layout.add_widget(confirm_button)

        Clock.schedule_interval(self.update_time, 1)
        self.add_widget(self.layout)

        # 新しく追加した部分: 色情報を格納
        #self.selected_color = [1, 1, 1, 1]

    def update_time(self, dt):
        self.time_label.text = self.get_japanese_time()

    def get_japanese_time(self):
        current_time = time.strftime("%H:%M:%S", time.localtime())
        return current_time

    def change_color(self, color):
        self.time_label.color = color
        # 新しく追加した部分: 色情報を格納
        self.selected_color = color

    def confirm_action(self, color, *args):
        print("確定ボタンが押されました。")
        print("選択された色:", self.selected_color)

    def switch_to_font_setting(self, instance):
        print("フォント設定画面に遷移します。")
        # 新しく追加した部分: 色情報を次の画面に渡す
        font_setting_screen = self.manager.get_screen('font_setting')
        font_setting_screen.selected_color = self.selected_color
        self.manager.current = 'font_setting'

class ClockScreen(Screen):

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

# TimeDisplayApp クラス内の build メソッド
class TimeDisplayApp(App):
    def build(self):
        # フォントのパスを追加
        resource_add_path(os.path.abspath("HoT_font"))

        self.sm = ScreenManager()

        main_screen = MainScreen(name='main')
        font_setting_screen = FontSettingScreen(name='font_setting')
        clock_screen = ClockScreen(name='clock')

        self.sm.add_widget(main_screen)
        self.sm.add_widget(font_setting_screen)
        self.sm.add_widget(clock_screen)

        return self.sm

if __name__ == '__main__':
    TimeDisplayApp().run()
