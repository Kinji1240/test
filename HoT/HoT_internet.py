import kivy
import logging
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
import subprocess
import csv
import os
import japanize_kivy

# ログの設定: レベルを DEBUG に設定し、フォーマットを指定
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class WiFiConnectApp(App):
    def build(self):
        self.csv_file_path = os.path.join("test", "HoT", "internet_data.csv")

        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        wifi_list = self.get_wifi_list()
        self.list_label = Label(text="Wi-Fi一覧:")
        layout.add_widget(self.list_label)

        for wifi in wifi_list:
            button = Button(text=wifi, on_press=self.show_wifi_popup)
            layout.add_widget(button)

        return layout

    def get_wifi_list(self):
        # ここでWi-Fi一覧を取得する方法を実装する（例: subprocessモジュールを使用してiwlistコマンドを実行）
        # この例では、仮のデータを返しています
        return ["Wi-Fi1", "Wi-Fi2", "Wi-Fi3"]

    def show_wifi_popup(self, instance):
        selected_wifi = instance.text

        # Popup内のコンテンツを構築
        content_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        connect_button = Button(text="接続する", on_press=lambda x: self.connect_wifi(selected_wifi))
        disconnect_button = Button(text="接続しない", on_press=lambda x: self.disconnect_wifi())
        content_layout.add_widget(connect_button)
        content_layout.add_widget(disconnect_button)

        # Popupを作成
        popup = Popup(title=f"{selected_wifi}に接続", content=content_layout, size_hint=(None, None), size=(300, 200))
        popup.open()

    def connect_wifi(self, selected_wifi):
        # ここで選択されたWi-Fiに接続する処理を実装する（例: subprocessモジュールを使用してwpa_supplicantを設定）

        self.log_to_csv("接続成功", selected_wifi)
        result_message = f"{selected_wifi} に接続しました。"
        self.show_result_popup("接続成功", result_message)

    def disconnect_wifi(self):
        # ここでWi-Fi接続を切断する処理を実装する（例: subprocessモジュールを使用してwpa_cliを実行）

        self.log_to_csv("切断失敗", "残念")
        result_message = "Wi-Fi接続を切断しました。"
        self.show_result_popup("切断成功", result_message)

    def log_to_csv(self, action, wifi_name):
        try:
            # CSVファイルが存在しない場合は新規作成
            if not os.path.exists(self.csv_file_path):
                os.makedirs(os.path.dirname(self.csv_file_path), exist_ok=True)
                with open(self.csv_file_path, 'w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow(['アクション', 'Wi-Fi名'])

            # CSVファイルにデータを追記
            with open(self.csv_file_path, 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([action, wifi_name])
            logger.info(f"CSVファイルにデータを追記しました: {action}, {wifi_name}")
        except Exception as e:
            logger.error(f"CSVファイルにデータを追記中にエラーが発生しました: {e}")

    def show_result_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

if __name__ == "__main__":
    logger.info("アプリケーションを開始します。")
    WiFiConnectApp().run()
