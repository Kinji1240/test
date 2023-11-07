from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import os
class MyApp(App):
    def build(self):
        # ルートレイアウト（BoxLayout）
        root_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # ボタンを作成
        button = Button(text='クリックしてください')
        button.bind(on_press=self.on_button_click)  # ボタンがクリックされたときの処理を指定

        # ボタンを中央に配置
        center_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(100, 50))
        center_layout.add_widget(button)
        root_layout.add_widget(center_layout)

        return root_layout

    def on_button_click(self, instance):
        # ボタンがクリックされたときに呼ばれる処理
        print('ボタンがクリックされました')
        os.system("python mainsys/teshaikei.py")
if __name__ == '__main__':
    MyApp().run()
