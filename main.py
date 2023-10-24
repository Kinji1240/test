from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import os
import japanize_kivy

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        button = Button(text='実行', size_hint=(None, None))
        button.bind(on_press=self.launch_main2)

        layout.add_widget(button)

        return layout

    def launch_main2(self, instance):
        # main2.pyを実行
        os.system('python main2.py')

if __name__ == '__main__':
    MainApp().run()