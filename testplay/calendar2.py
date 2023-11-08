from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
import japanize_kivy

class CalendarApp(App):
    def build(self):
        layout = GridLayout(cols=7)
        self.days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

        for day in self.days:
            layout.add_widget(Button(text=day, background_normal='', background_color=(0.1, 0.5, 0.6, 1)))

        for day in range(1, 32):  # 1から31までの日付ボタンを作成
            day_button = Button(text=str(day), background_normal='', background_color=(0.7, 0.7, 0.7, 1))
            day_button.bind(on_release=self.show_popup)
            layout.add_widget(day_button)

        return layout

    def show_popup(self, instance):
        popup_content = GridLayout(rows=3)
        popup_content.add_widget(TextInput(hint_text="予定を入力してください"))
        popup_content.add_widget(Button(text="OK", on_release=self.close_popup))
        popup_content.add_widget(Button(text="キャンセル", on_release=self.dismiss_popup))

        self.popup = Popup(title="予定", content=popup_content, size_hint=(None, None), size=(300, 200))
        self.popup.open()

    def close_popup(self, instance):
        self.popup.dismiss()

    def dismiss_popup(self, instance):
        self.popup.dismiss()

if __name__ == '__main__':
    CalendarApp().run()