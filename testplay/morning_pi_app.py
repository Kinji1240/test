from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import sys
import japanize_kivy

class MorningPiApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)
        title_label = Label(text="朝の目覚めにこのシステム", font_size=24)
        subtitle_label = Label(text="Morning Pi", font_size=16)
        next_button = Button(text="次へ", size_hint=(None, None))
        next_button.bind(on_release=self.on_next_button_click)
        layout.add_widget(title_label)
        layout.add_widget(subtitle_label)
        layout.add_widget(next_button)
        return layout

    def on_next_button_click(self, instance):
        # 画面遷移を実行
        self.stop()  # 現在のアプリを終了
        Initial2App().run()  # 別のアプリを起動

if __name__ == "__main__":
    MorningPiApp().run()

    