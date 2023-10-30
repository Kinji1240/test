from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
import japanize_kivy

class CalendarApp(App):
    def build(self):
        layout = GridLayout(cols=7, spacing=5, size_hint=(None, None), width=420)

        self.days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

        for day in self.days:
            layout.add_widget(Label(text=day, size_hint_y=None, height=44, color=(0.1, 0.5, 0.6, 1)))

        self.day_buttons = []

        for day_num in range(1, 32):
            day_button = Button(text=str(day_num), size_hint=(None, None), size=(60, 60), background_color=(0.5, 0.7, 0.8, 1), on_release=self.show_popup)
            layout.add_widget(day_button)
            self.day_buttons.append(day_button)

        self.spinner = Spinner(text='Select Month', values=[str(i) for i in range(1, 13)], size_hint=(None, None), size=(150, 44), pos_hint={'center_x': 0.5})
        self.spinner.bind(text=self.on_spinner_select)

        self.layout = BoxLayout(orientation='vertical', spacing=5, padding=5)
        self.layout.add_widget(self.spinner)
        self.layout.add_widget(layout)

        return self.layout

    def on_spinner_select(self, instance, value):
        selected_month = instance.text
        days_in_month = int(selected_month)

        for i, day_button in enumerate(self.day_buttons):
            if i < days_in_month:
                day_button.disabled = False
            else:
                day_button.disabled = True

    def show_popup(self, instance):
        if instance.text != '':
            popup_content = BoxLayout(orientation='vertical', spacing=5, padding=5)
            popup_content.add_widget(Label(text=f"予定 ({self.spinner.text}/{instance.text})", size_hint_y=None, height=44))
            popup_content.add_widget(Button(text="予定を入力", on_release=self.show_input))
            popup_content.add_widget(Button(text="閉じる", on_release=self.dismiss_popup))

            self.popup = Popup(title=f"予定 ({self.spinner.text}/{instance.text})", content=popup_content, size_hint=(None, None), size=(300, 150), pos_hint={'center_x': 0.5, 'center_y': 0.5})
            self.popup.open()

    def show_input(self, instance):
        self.popup.dismiss()

        input_popup_content = BoxLayout(orientation='vertical', spacing=5, padding=5)
        input_popup_content.add_widget(TextInput(hint_text="予定を入力してください", size_hint_y=None, height=44))
        input_popup_content.add_widget(Button(text="OK", on_release=self.dismiss_input_popup))

        self.input_popup = Popup(title=f"予定入力", content=input_popup_content, size_hint=(None, None), size=(300, 150), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.input_popup.open()

    def dismiss_input_popup(self, instance):
        self.input_popup.dismiss()

    def dismiss_popup(self, instance):
        self.popup.dismiss()

if __name__ == '__main__':
    CalendarApp().run()
