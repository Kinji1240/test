from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.clock import Clock
import time

class TimeDisplayApp(App):
    def build(self):
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

        Clock.schedule_interval(self.update_time, 1)  # 1秒ごとに時間を更新

        return self.layout

    def update_time(self, dt):
        self.time_label.text = self.get_japanese_time()

    def get_japanese_time(self):
        current_time = time.strftime("%H:%M:%S", time.localtime())
        return current_time

    def change_color(self, color):
        self.time_label.color = color

if __name__ == '__main__':
    TimeDisplayApp().run()