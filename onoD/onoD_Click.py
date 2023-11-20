from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.clock import Clock
import os

class LongPressButton(Button):
    def __init__(self, **kwargs):
        super(LongPressButton, self).__init__(**kwargs)
        self.long_press_time = 2  # 長押しを定義する時間（秒）
        self.long_press_event = None

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.long_press_event = Clock.schedule_once(self.on_long_press, self.long_press_time)
        return super(LongPressButton, self).on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            if self.long_press_event:
                self.long_press_event.cancel()
                self.long_press_event = None
            else:
                self.on_short_press()  # 短押しの場合の処理を呼び出す

    def on_long_press(self, dt):
        print("長押しされました")
        os.system("python onoD_main.py")

    def on_short_press(self): 
        print("普通にタッチされました")

class LongPressApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        button = LongPressButton(text='長押しボタン')
        layout.add_widget(button)
        return layout

if __name__ == '__main__':
    LongPressApp().run()
