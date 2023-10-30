from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
import calendar

class CalendarApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # 月の選択用スピナーを作成
        self.months = [calendar.month_name[i] for i in range(1, 13)]
        self.spinner = Spinner(text='Select Month', values=self.months, size_hint=(None, None), size=(200, 44))
        self.spinner.bind(text=self.on_spinner_select)
        layout.add_widget(self.spinner)

        # ボタン表示用のBoxLayout
        self.button_layout = BoxLayout(orientation='horizontal', spacing=10)
        layout.add_widget(self.button_layout)

        return layout

    def on_spinner_select(self, instance, value):
        # 選択された月の日数を取得
        selected_month = instance.text
        days_in_month = calendar.monthrange(2023, self.months.index(selected_month) + 1)[1]

        # ボタンを作成・表示
        self.button_layout.clear_widgets()
        for day in range(1, days_in_month + 1):
            button = Button(text=str(day), size_hint=(None, None), size=(50, 50))
            self.button_layout.add_widget(button)

if __name__ == '__main__':
    CalendarApp().run()