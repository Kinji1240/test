from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
import os
import japanize_kivy

class MainApp(App):
    def build(self):
        layout = GridLayout(cols=1, spacing=10, padding=10)

        # タイトルのラベル
        title_label = Label(
            text="ほしい機能を選んでね",
            font_size=24,
            size_hint_y=None,
            height=50,
            halign="center",
        )

        button1 = Button(text="実行", size_hint=(None, None))
        button1.bind(on_press=self.launch_main2)

        button2 = Button(text="別の機能を実行", size_hint=(None, None))
        button2.bind(on_press=self.launch_main3)

        layout.add_widget(title_label)
        layout.add_widget(Widget())  # 上部の余白用
        layout.add_widget(button1)
        layout.add_widget(button2)

        return layout

    def launch_main2(self, instance):
        # main2.pyを実行
        os.system("python main2.py")

    def launch_main3(self, instance):
        # main3.pyを実行
        os.system("python main3.py")

if __name__ == "__main__":
    MainApp().run()