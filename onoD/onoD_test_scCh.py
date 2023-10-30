from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
import calendar

class CalendarApp(App):
    def build(self):
        layout = GridLayout(cols=7)
        self.days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

        for day in self.days:
            layout.add_widget(Button(text=day, background_normal='', background_color=(0.1, 0.5, 0.6, 1)))

        self.day_buttons = []

        for _ in range(35):
            day_button = Button()
            day_button.bind(on_release=self.show_popup)
            layout.add_widget(day_button)
            self.day_buttons.append(day_button)

        self.spinner = Spinner(text='Select Month', values=[calendar.month_name[i] for i in range(1, 13)])
        self.spinner.bind(text=self.on_spinner_select)
        layout.add_widget(self.spinner)

        return layout

    def on_spinner_select(self, instance, value):
        selected_month = instance.text
        days_in_month = calendar.monthrange(2023, list(calendar.month_name).index(selected_month))[1]

        for i, day_button in enumerate(self.day_buttons):
            if i < days_in_month:
                day_button.text = str(i + 1)
                day_button.disabled = False
            else:
                day_button.text = ''
                day_button.disabled = True

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
