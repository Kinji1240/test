from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.text import LabelBase
from kivy.clock import Clock
import csv
import os

class ClockApp(App):
    def build(self):
        # 設定ファイルからフォントと色の情報を読み取る
        font, color = self.read_settings()

        # フォントを設定
        LabelBase.register(name="custom", fn_regular=font)

        # 時計の表示用のラベルを作成
        clock_label = Label(text="12:00", font_name="custom", font_size=50, color=color)

        # レイアウトを作成してラベルを追加
        layout = BoxLayout(orientation="vertical", padding=10)
        layout.add_widget(clock_label)

        # 時計を更新する関数をスケジュールに登録
        Clock.schedule_interval(self.update_clock, 1)

        return layout

    def read_settings(self):
        # 設定ファイルからフォントと色の情報を読み取る
        font = ""
        color = []
        settings_path = os.path.join(os.getcwd(), "TEST", "testplay", "CSV", "settings.csv")
        with open(settings_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                font = row["font"]
                color = [float(value) for value in row["color"].split(",")]

        return font, color

    def update_clock(self, *args):
        # 時計の時間を更新
        pass  # ここに実際の時計の更新ロジックを追加

if __name__ == "__main__":
    ClockApp().run()
