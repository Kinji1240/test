from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
import os
import csv
import japanize_kivy

class InternetScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(InternetScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # インターネット接続ステータスを表示するラベル
        self.status_label = Label(text='インターネットに接続しますか？', font_size='20sp', size_hint=(1, 0.5))
        self.add_widget(self.status_label)

        # はい・いいえボタンを配置するGridLayout
        button_layout = GridLayout(cols=2, size_hint=(1, 0.5))
        self.add_widget(button_layout)

        yes_button = Button(text='はい', size_hint=(0.4, 0.5), on_press=self.connect_to_internet)
        button_layout.add_widget(yes_button)

        no_button = Button(text='いいえ', size_hint=(0.4, 0.5), on_press=self.disconnect_from_internet)
        button_layout.add_widget(no_button)

    def connect_to_internet(self, instance):
        # インターネットに接続する処理
        print("インターネットに接続しました")
        self.show_result_popup("インターネットに接続しました")

    def disconnect_from_internet(self, instance):
        # インターネットから切断する処理
        print("インターネットに接続しませんでした")
        self.show_result_popup("インターネットに接続しませんでした")

    def show_result_popup(self, result):
        popup_content = BoxLayout(orientation='vertical')
        popup_content.add_widget(Label(text=result, font_size='18sp'))
        close_button = Button(text='閉じる', size_hint=(1, 0.3), on_press=lambda instance: self.dismiss_popup(instance))
        popup_content.add_widget(close_button)

        popup = Popup(title='結果', content=popup_content, size_hint=(0.6, 0.4))
        popup.open()

    def dismiss_popup(self, instance):
        if isinstance(instance, Button):  # Button オブジェクトであるか確認
            instance.parent.parent.dismiss()  # 2回 parent して Popup にアクセス

class InternetApp(App):
    def build(self):
        return InternetScreen()

if __name__ == '__main__':
    InternetApp().run()
