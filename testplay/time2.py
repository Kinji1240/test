from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.button import Button
from kivy.clock import Clock as kivyClock
from kivy.properties import BooleanProperty
from datetime import datetime

class ClockSwitcherApp(App):
    def build(self):
        self.analog_clock_widget = AnalogClock()
        self.digital_clock_widget = DigitalClock()
        self.digital_clock_widget.hide()

        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.clock_type_label = Label(text="アナログ時計", size_hint=(1, None), height=50, halign="center")

        switch_button = Button(text="切り替え")
        switch_button.bind(on_release=self.switch_clock)

        layout.add_widget(self.clock_type_label)
        layout.add_widget(self.analog_clock_widget)
        layout.add_widget(self.digital_clock_widget)
        layout.add_widget(switch_button)

        return layout

    def switch_clock(self, instance):
        if self.analog_clock_widget.is_shown:
            self.analog_clock_widget.hide()
            self.digital_clock_widget.show()
            self.clock_type_label.text = "デジタル時計"
        else:
            self.digital_clock_widget.hide()
            self.analog_clock_widget.show()
            self.clock_type_label.text = "アナログ時計"

class ClockWidget(Widget):
    is_shown = BooleanProperty(False)

    def show(self):
        self.is_shown = True

    def hide(self):
        self.is_shown = False

class AnalogClock(ClockWidget):
    def __init__(self, **kwargs):
        super(AnalogClock, self).__init__(**kwargs)
        kivyClock.schedule_interval(self.update, 1)

    def update(self, *args):
        now = datetime.now()
        seconds = now.second
        self.rotation = (seconds / 60) * 360

    def on_size(self, instance, value):
        self.draw_clock()

    def draw_clock(self):
        self.canvas.clear()
        with self.canvas:
            Color(0, 0, 0)
            Ellipse(pos=(self.center_x - self.width / 2, self.center_y - self.height / 2), size=(self.width, self.height))
            Color(1, 1, 1)
            Line(circle=(self.center_x, self.center_y, self.width / 2 - 2), width=2)
            Color(0, 0, 0)
            Line(points=[self.center_x, self.center_y, self.center_x + self.width / 2 * 0.8 * 0.7, self.center_y], width=2)
            Color(1, 0, 0)
            Line(points=[self.center_x, self.center_y, self.center_x + self.width / 2 * 0.8 * 0.7, self.center_y], width=1, cap='none')
            Line(points=[self.center_x, self.center_y, self.center_x + self.width / 2 * 0.8 * 0.7, self.center_y], width=4, cap='none')

class DigitalClock(ClockWidget):
    pass

if __name__ == '__main__':
    ClockSwitcherApp().run()