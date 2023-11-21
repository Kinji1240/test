from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from datetime import datetime

import subprocess


class MultiWidgetApp(App):
    def run_clock_generator():
        subprocess.run(["python", "onoD_1day_weather.py"])


if __name__ == '__main__':
    MultiWidgetApp().run()