from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout

class RedDigitalClockApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text='00:00:00', font_size=50, color=(1, 0, 0, 1))  # 赤いテキストカラー
        layout.add_widget(self.label)
        Clock.schedule_interval(self.update_time, 1)
        return layout

    def update_time(self, dt):
        import time
        current_time = time.strftime('%H:%M:%S')
        self.label.text = current_time

if __name__ == '__main__':
    RedDigitalClockApp().run()
