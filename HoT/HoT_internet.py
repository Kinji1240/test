import csv
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import japanize_kivy
from plyer import wifi

class InternetScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(InternetScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # インターネット接続ステータスを表示するラベル
        self.status_label = Label(text='インターネットに接続しますか？', font_size='20sp', size_hint=(1, 0.5))
        self.add_widget(self.status_label)

        # はい・いいえボタンを配置するBoxLayout
        button_layout = BoxLayout(size_hint=(1, 0.1))
        self.add_widget(button_layout)

        yes_button = Button(text='はい', size_hint=(0.5, 1), on_press=self.connect_to_internet)
        button_layout.add_widget(yes_button)

        no_button = Button(text='いいえ', size_hint=(0.5, 1), on_press=self.disconnect_from_internet)
        button_layout.add_widget(no_button)

        # CSVファイルのヘッダーを書き込む
        with open('test/HoT/internet_data.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['操作', '結果'])

    def connect_to_internet(self, instance):
        print("インターネットに接続しました")
        self.show_result_popup("インターネットに接続しました")
        # CSVファイルにデータを書き込む
        self.write_to_csv("はい", "成功")
        # Wi-Fiの設定画面を開く（コメントアウトまたは削除）
        # wifi.open_network_settings()

    def disconnect_from_internet(self, instance):
        print("インターネットに接続しませんでした")
        self.show_result_popup("インターネットに接続しませんでした")
        # CSVファイルにデータを書き込む
        self.write_to_csv("いいえ", "失敗")

    def write_to_csv(self, action, result):
        # CSVファイルにデータを書き込む
        with open('test/HoT/internet_data.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([action, result])

    def show_result_popup(self, result):
        popup_content = BoxLayout(orientation='vertical')
        popup_content.add_widget(Label(text=result, font_size='18sp'))
        close_button = Button(text='閉じる', size_hint=(1, 0.3), on_press=lambda instance: self.dismiss_popup(instance))
        popup_content.add_widget(close_button)

        # Popupインスタンスを保存
        self._popup = Popup(title='結果', content=popup_content, size_hint=(0.6, 0.4))
        self._popup.open()

    def dismiss_popup(self, instance):
        if isinstance(instance, Button):
            # 保存したPopupインスタンスを閉じる
            self._popup.dismiss()

class InternetApp(App):
    def build(self):
        return InternetScreen()

if __name__ == '__main__':
    InternetApp().run()
