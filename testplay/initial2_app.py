from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class Initial2App(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)
        title_label = Label(text="Initial2 Screen", font_size=24)
        back_button = Button(text="戻る", size_hint=(None, None))
        back_button.bind(on_release=self.on_back_button_click)
        layout.add_widget(title_label)
        layout.add_widget(back_button)
        return layout

    def on_back_button_click(self, instance):
        # 画面遷移を実行
        self.stop()  # 現在のアプリを終了
        MorningPiApp().run()  # メインのアプリを再度起動

if __name__ == "__main__":
    Initial2App().run()