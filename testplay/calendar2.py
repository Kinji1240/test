import csv
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from datetime import datetime
import calendar

class CalendarGrid(GridLayout):
    def __init__(self, app, csv_data, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        self.csv_data = csv_data
        self.cols = 7
        self.populate()

    def populate(self):
        self.clear_widgets()
        
        # 曜日ラベルを追加
        for day in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]:
            label = Label(text=day, size_hint_y=None, height=40)
            self.add_widget(label)
            
        today = datetime.now().day
        for week in calendar.monthcalendar(self.app.year, self.app.month):
            for day in week:
                if day == 0:
                    label = Label(text="", size_hint_y=None, height=40)
                    self.add_widget(label)
                else:
                    btn = Button(text=str(day), size_hint_y=None, height=40)
                    if day == today:
                        btn.background_color = [1, 0.5, 0.5, 1]  # highlight today
                    btn.bind(on_press=self.app.on_day_selected)
                    self.add_widget(btn)

class CalendarApp(App):
    def build(self):
        self.tasks = {}
        self.month = datetime.now().month
        self.year = datetime.now().year

        # CSVファイルの読み込み（UTF-8エンコーディング）
        self.csv_data = {}
        with open('schedules.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                date = row['Date']
                time = row['Time']
                person = row['Person']
                content = row['Content']
                key = f"{date},{time}"
                if key not in self.csv_data:
                    self.csv_data[key] = {'Person': person, 'Content': content}

        self.root_layout = BoxLayout(orientation='vertical')

        self.calendar_layout = BoxLayout(size_hint_y=0.7)
        self.calendar_grid = CalendarGrid(app=self, csv_data=self.csv_data)
        self.calendar_layout.add_widget(self.calendar_grid)
        self.root_layout.add_widget(self.calendar_layout)

        self.selected_label = Label(text=f"Selected Date: {self.month}/??/{self.year}", size_hint_y=0.1)
        self.root_layout.add_widget(self.selected_label)

        self.time_spinner = Spinner(text="Select Time", values=[f"{i:02d}:00" for i in range(24)], size_hint=(0.5, 0.1))
        self.root_layout.add_widget(self.time_spinner)

        self.task_view = TextInput(hint_text='Enter your task for the selected time', size_hint_y=0.2)
        self.root_layout.add_widget(self.task_view)

        controls_layout = BoxLayout(size_hint_y=0.1)
        prev_btn = Button(text="< Prev")
        prev_btn.bind(on_press=self.prev_month)
        controls_layout.add_widget(prev_btn)
        
        next_btn = Button(text="Next >")
        next_btn.bind(on_press=self.next_month)
        controls_layout.add_widget(next_btn)

        save_btn = Button(text="Save Task")
        save_btn.bind(on_press=self.save_task)
        controls_layout.add_widget(save_btn)

        self.root_layout.add_widget(controls_layout)

        # 月のプルダウンメニューを追加
        self.month_spinner = Spinner(text="Select Month", values=[calendar.month_name[i] for i in range(1, 13)], size_hint=(0.5, 0.1))
        self.month_spinner.bind(text=self.on_month_select)
        self.root_layout.add_widget(self.month_spinner)

        # Display task for today at the selected time
        self.on_day_selected(Button(text=str(datetime.now().day)))

        return self.root_layout

    def on_day_selected(self, instance):
        date_key = f"{self.year}-{self.month}-{instance.text},{self.time_spinner.text}"
        self.selected_label.text = f"Selected Date: {self.month}/{instance.text}/{self.year} at {self.time_spinner.text}"
        task_info = self.csv_data.get(date_key, {"Person": "", "Content": ""})
        person = task_info.get("Person", "")
        content = task_info.get("Content", "")
        self.task_view.text = f"Person: {person}\nContent: {content}"

    def save_task(self, instance):
        date_key = f"{self.year}-{self.month}-{self.selected_label.text.split('/')[1]},{self.time_spinner.text}"
        person = self.task_view.text.split('\n')[0].replace("Person: ", "")
        content = self.task_view.text.split('\n')[1].replace("Content: ", "")
        self.csv_data[date_key] = {'Person': person, 'Content': content}

    def prev_month(self, instance):
        self.month -= 1
        if self.month < 1:
            self.month = 12
            self.year -= 1
        self.update_calendar()

    def next_month(self, instance):
        self.month += 1
        if self.month > 12:
            self.month = 1
            self.year += 1
        self.update_calendar()

    def on_month_select(self, instance, value):
        self.month = list(calendar.month_name).index(instance.text)
        self.update_calendar()

    def update_calendar(self):
        self.calendar_grid.populate()
        self.selected_label.text = f"Selected Date: {self.month}/??/{self.year} at {self.time_spinner.text}"
        self.task_view.text = ""

if __name__ == '__main__':
    CalendarApp().run()