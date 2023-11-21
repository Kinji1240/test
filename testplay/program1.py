from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class NestedWindowApp(App):
    def build(self):
        # メインウィンドウのレイアウト
        main_layout = BoxLayout(orientation='vertical')

        # メインウィンドウに配置されるボタン
        main_button = Button(text='Main Window Button')
        main_button.bind(on_press=self.on_main_button_press)  # ボタンが押されたときのイベントを設定
        main_layout.add_widget(main_button)

        # サブウィンドウのレイアウト
        sub_layout = BoxLayout(orientation='vertical')

        # サブウィンドウに配置されるボタン
        sub_button = Button(text='Sub Window Button')
        sub_button.bind(on_press=self.on_sub_button_press)  # ボタンが押されたときのイベントを設定
        sub_layout.add_widget(sub_button)

        # メインウィンドウにサブウィンドウを配置
        main_layout.add_widget(sub_layout)

        # 結果を表示するためのラベル
        self.result_label = Label(text='Result will be displayed here.')
        main_layout.add_widget(self.result_label)

        return main_layout

    def on_main_button_press(self, instance):
        self.result_label.text = 'Main button pressed!'

    def on_sub_button_press(self, instance):
        self.result_label.text = 'Sub button pressed!'

if __name__ == '__main__':
    NestedWindowApp().run()
