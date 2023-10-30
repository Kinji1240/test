from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

import japanize_kivy

class CalendarApp(App):
    def build(self):
        self.layout = GridLayout(cols=7)
        self.days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        self.current_year = 2022
        self.current_month = 1

        self.create_calendar()

        return self.layout

    def create_calendar(self):
        self.layout.clear_widgets()

        # 月の日数を計算
        days_in_month = 31
        if self.current_month in [4, 6, 9, 11]:
            days_in_month = 30
        elif self.current_month == 2:
            if (self.current_year % 4 == 0 and self.current_year % 100 != 0) or (self.current_year % 400 == 0):
                days_in_month = 29
            else:
                days_in_month = 28

        for day in self.days:
            self.layout.add_widget(Label(text=day, halign='center', valign='middle', bold=True))

        day_number = 1
        for _ in range(6):  # 6行まで表示
            for _ in range(7):  # 1週間分の日付
                if day_number <= days_in_month:
                    with self.layout.canvas.before:
                        Color(0.1, 0.5, 0.6, 1)
                        Rectangle(pos=self.layout.pos, size=self.layout.size)
                    day_button = Button(text=str(day_number), background_color=(0.7, 0.7, 0.7, 1))
                    day_button.bind(on_release=self.show_popup)
                    self.layout.add_widget(day_button)
                    day_number += 1

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