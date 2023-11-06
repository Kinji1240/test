from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

class MainApp(App):
    def build(self):
        # メインのレイアウト
        layout = BoxLayout(orientation='horizontal')

        # BlueDigitalClockAppを表示
        blue_clock_app = Builder.load_file("blue_clock.kv")
        layout.add_widget(blue_clock_app)

        # RedDigitalClockAppを表示
        red_clock_app = Builder.load_file("red_clock.kv")
        layout.add_widget(red_clock_app)

        return layout

if __name__ == '__main__':
    MainApp().run()