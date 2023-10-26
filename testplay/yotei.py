from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class WeeklyCalendarApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        week_schedule = [
            ("Sunday", ""),
            ("Monday", ""),
            ("Tuesday", ""),
            ("Wednesday", ""),
            ("Thursday", ""),
            ("Friday", ""),
            ("Saturday", "")
        ]

        for day, schedule in week_schedule:
            day_label = Label(text=day, bold=True)
            text_input = TextInput(text=schedule, multiline=False)
            layout.add_widget(day_label)
            layout.add_widget(text_input)
        
        return layout

if __name__ == '__main__':
    WeeklyCalendarApp().run()