from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
import japanize_kivy

class HelloWorldApp(App):
    def build(self):
        self.label = Label(text='Hello', font_size='50sp')
        Clock.schedule_interval(self.update_label, 10)  # 10秒ごとにupdate_labelを呼び出す
        return self.label

    def update_label(self, dt):
        if self.label.text == 'Hello':
            self.label.text = 'おはよう'
        else:
            self.label.text = 'Hello'

if __name__ == '__main__':
    HelloWorldApp().run()