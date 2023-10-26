from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
import japanize_kivy

class MyKivyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # 背景画像の初期設定
        self.background_sources = ['C:/Users/204004/Desktop/font/light-gray-concrete-wall.jpg', 'C:/Users/204004/Desktop/font/cat.gif']
        self.current_background_index = 0
        with layout.canvas.before:
            self.background = Rectangle(source=self.background_sources[self.current_background_index], pos=(0, 0), size=Window.size)

        label = Label(text='Kivyサンプルアプリ', font_size=24)

        # ボタンを配置する新しいBoxLayoutを作成
        button_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=100, spacing=10)
        confirm_button = Button(text='確定', on_release=self.confirm_action)
        button_layout.add_widget(confirm_button)

        layout.add_widget(label)
        layout.add_widget(button_layout)
        layout.bind(on_touch_down=self.change_background)

        return layout

    def change_background(self, instance, touch):
        # タッチ操作で背景を切り替える
        if self.current_background_index == 0:
            self.current_background_index = 1
        else:
            self.current_background_index = 0

        self.background.source = self.background_sources[self.current_background_index]

    def confirm_action(self, instance):
        # 確定ボタンが押されたときの処理をここに追加
        print("確定ボタンが押されました")

if __name__ == '__main__':
    MyKivyApp().run()