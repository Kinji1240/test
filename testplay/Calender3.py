from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
import japanize_kivy
import datetime

class CalendarWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(CalendarWidget, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.days = ["月", "火", "水", "木", "金", "土", "日"]  # 月曜日から始まる曜日順に変更
        self.current_year = 2023
        self.current_month = 1

        self.create_calendar()

    def create_calendar(self):
        self.clear_widgets()

        # 曜日ラベルを追加
        days_layout = GridLayout(cols=7)
        for day in self.days:
            days_layout.add_widget(Label(text=day, halign='center', valign='middle', bold=True))
        self.add_widget(days_layout)

        # 月の日数を計算
        first_day = datetime.date(self.current_year, self.current_month, 1)
        days_in_month = (first_day.replace(month=first_day.month % 12 + 1, day=1) - first_day).days

        # 月の1日の曜日を取得 (0=月曜, 6=日曜)
        first_day_of_week = first_day.weekday()

        # 月の1日が月曜日でない場合、前月の日を埋める
        for _ in range(first_day_of_week):
            days_layout.add_widget(Label(text=""))

        day_number = 1
        for _ in range(6):  # 6行まで表示
            for _ in range(7):  # 1週間分の日付
                if day_number <= days_in_month:
                    with days_layout.canvas.before:
                        Color(0.1, 0.5, 0.6, 1)
                        Rectangle(pos=days_layout.pos, size=days_layout.size)
                    day_button = Button(text=str(day_number), background_color=(0.7, 0.7, 0.7, 1))
                    day_button.bind(on_release=self.show_popup)
                    days_layout.add_widget(day_button)
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

class CalendarApp(App):
    def build(self):
        return CalendarWidget()

if __name__ == '__main__':
    CalendarApp().run()