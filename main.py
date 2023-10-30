from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import japanize_kivy

class CalendarApp(App):
    def build(self):
        self.layout = GridLayout(cols=7)
        self.days = ["日", "月", "火", "水", "木", "金", "土"]
        self.current_year = 2023 
        self.current_month = 1

        self.create_calendar()

        control_layout = GridLayout(cols=3)
        prev_month_button = Button(text="前月", on_release=self.prev_month)
        next_month_button = Button(text="次月", on_release=self.next_month)
        control_layout.add_widget(prev_month_button)
        control_layout.add_widget(Label(text=f"{self.current_year}年{self.current_month}月"))
        control_layout.add_widget(next_month_button)

        root_layout = GridLayout(rows=2)
        root_layout.add_widget(control_layout)
        root_layout.add_widget(self.layout)

        return root_layout

    def create_calendar(self):
        self.layout.clear_widgets()
        for day in self.days:
            self.layout.add_widget(Label(text=day))

        for day in range(1, 32):  # 1から31までの日付ボタンを作成
            day_button = Button(text=str(day))
            day_button.bind(on_release=self.show_popup)
            self.layout.add_widget(day_button)

    def prev_month(self, instance):
        if self.current_month == 1:
            self.current_month = 12
            self.current_year -= 1
        else:
            self.current_month -= 1
        self.create_calendar()

    def next_month(self, instance):
        if self.current_month == 12:
            self.current_month = 1
            self.current_year += 1
        else:
            self.current_month += 1
        self.create_calendar()

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