from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from datetime import datetime

import subprocess


class MultiWidgetApp(App):
    def build(self):
        layout = FloatLayout()
        self.result_labels = []  # clock_labelsをリストとして宣言

        # ウィジェットの座標データを変数として定義
        widget_positions = [
            (100, 100),
            (200, 200)
        ]

        
        external_program_paths = [
        "test\onoD\onoD_ok_list\onoD_weather\onoD_1day_weather.py",
        "test\onoD\onoD_error.py"
        ]
        
        weather_label = Label(text = self.run_external_program(external_program_paths[0]))
        weather_label.pos = widget_positions(50,50)
        layout.add_widget(weather_label)
        self.result_labels.append(weather_label)

        tigers_label = widget_positions(50, 100)
        layout.add_widget(tigers_label)
        self.result_labels.append(tigers_label)
        
        Clock.schedule_interval(lambda dt, label=weather_label, path=external_program_paths[0]: self.update_result(dt, label, path), 1)



        return layout
    def run_external_program(self, file_path):
        # 別のPythonファイルを実行し、結果を取得
        result = subprocess.run(["python", file_path], capture_output=True, text=True)
        return result.stdout.strip()
    
    def update_result(self, dt, label, file_path):
        # 1秒ごとに外部プログラムを実行し、結果を更新
        label.text = self.run_external_program(file_path)


if __name__ == '__main__':
    MultiWidgetApp().run()
