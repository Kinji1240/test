import csv
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
import japanize_kivy

class RegistrationScreen(Screen):
    def __init__(self, **kwargs):
        super(RegistrationScreen, self).__init__(**kwargs)
        b = BoxLayout(orientation='vertical')

        # 年月日のSpinnerを追加
        self.year_spinner = Spinner(text='2023', values=('2020', '2021', '2022', '2023', '2024'))
        self.month_spinner = Spinner(text='1', values=[str(i) for i in range(1, 13)])
        self.day_spinner = Spinner(text='1', values=[str(i) for i in range(1, 32)])

        date_layout = BoxLayout()
        date_layout.add_widget(self.year_spinner)
        date_layout.add_widget(self.month_spinner)
        date_layout.add_widget(self.day_spinner)

        self.time_input = TextInput(hint_text="時間")
        self.person_input = TextInput(hint_text="登録する人")
        self.content_input = TextInput(hint_text="内容")
        self.submit_button = Button(text="予定を追加")
        self.submit_button.bind(on_press=self.add_schedule)

        b.add_widget(date_layout)
        b.add_widget(self.time_input)
        b.add_widget(self.person_input)
        b.add_widget(self.content_input)
        b.add_widget(self.submit_button)

        self.add_widget(b)

    def add_schedule(self, instance):
        year = self.year_spinner.text
        month = self.month_spinner.text
        day = self.day_spinner.text
        date = f"{year}-{month}-{day}"
        time = self.time_input.text
        person = self.person_input.text
        content = self.content_input.text

        self.manager.get_screen('display').update_schedule(date, time, person, content)
        self.manager.current = 'display'

class DisplayScreen(Screen):
    def __init__(self, **kwargs):
        super(DisplayScreen, self).__init__(**kwargs)
        self.schedule_data = {}
        
        # Root layout
        self.root_layout = BoxLayout(orientation='vertical')
        
        # Date input for schedule checking
        self.date_check_input = TextInput(hint_text="確認する日付 (例: 2023-10-29)", size_hint_y=None, height=44)
        self.root_layout.add_widget(self.date_check_input)

        # Button to check the schedule of the specified date
        self.check_button = Button(text="日程を確認", size_hint_y=None, height=50)
        self.check_button.bind(on_press=self.check_schedule)
        self.root_layout.add_widget(self.check_button)

        # Schedules layout
        self.layout = BoxLayout(orientation='vertical')
        self.root_layout.add_widget(self.layout)

        # Return button
        self.return_button = Button(text="戻る", size_hint_y=None, height=50)
        self.return_button.bind(on_press=self.go_back)
        self.root_layout.add_widget(self.return_button)

        self.add_widget(self.root_layout)

    def go_back(self, instance):
        self.manager.current = 'register'

    def check_schedule(self, instance):
        target_date = self.date_check_input.text
        self.manager.get_screen('details').show_details(target_date)
        self.manager.current = 'details'

    def update_schedule(self, date, time, person, content):
        if date not in self.schedule_data:
            self.schedule_data[date] = []
        self.schedule_data[date].append((time, person, content))
        self.display_schedules()
        self.save_to_csv()  # 予定を追加するたびにCSVに保存

    def load_from_csv(self):
        try:
            with open('schedules.csv', 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)  # ヘッダーをスキップ
                for row in reader:
                    date, time, person, content = row
                    if date not in self.schedule_data:
                        self.schedule_data[date] = []
                    self.schedule_data[date].append((time, person, content))
        except FileNotFoundError:
            pass

    def save_to_csv(self):
        with open('schedules.csv', 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Time", "Person", "Content"])  # ヘッダー
            for date, schedules in self.schedule_data.items():
                for time, person, content in schedules:
                    writer.writerow([date, time, person, content])

    def display_schedules(self):
        self.layout.clear_widgets()

        for date, schedules in sorted(self.schedule_data.items(), key=lambda x: x[0]):
            date_label = Label(text=f"日付: {date}", size_hint_y=None, height=44)
            self.layout.add_widget(date_label)

            for time, person, content in schedules:
                schedule_label = Label(text=f"時間: {time}\n登録する人: {person}\n内容: {content}", size_hint_y=None, height=66)
                self.layout.add_widget(schedule_label)

class DetailsScreen(Screen):    
    def __init__(self, **kwargs):
        super(DetailsScreen, self).__init__(**kwargs)
        self.current_date = ""
        self.layout = BoxLayout(orientation='vertical')

        # Upper space for future customization
        self.upper_space = BoxLayout(size_hint_y=0.3) # Adjust as necessary
        self.layout.add_widget(self.upper_space)

        # Content container
        self.content_layout = BoxLayout(size_hint_y=0.6, orientation='vertical')
        self.layout.add_widget(self.content_layout)

        # Add a button to go back to the first screen at the bottom
        self.return_to_main_button = Button(text="最初の画面に戻る", size_hint_y=0.1)
        self.return_to_main_button.bind(on_press=self.return_to_main)
        self.layout.add_widget(self.return_to_main_button)

        self.add_widget(self.layout)

    def return_to_main(self, instance):
        self.manager.current = 'register'

    def show_details(self, date):
        self.layout.clear_widgets()
        self.current_date = date

        schedules = self.manager.get_screen('display').schedule_data.get(date, [])
        if schedules:
            for index, (time, person, content) in enumerate(schedules):
                detail_layout = BoxLayout(size_hint_y=None, height=66, orientation='horizontal')
                
                schedule_label = Label(text=f"時間: {time}\n登録する人: {person}\n内容: {content}", size_hint_x=0.8)
                detail_layout.add_widget(schedule_label)
                
                delete_button = Button(text="削除", size_hint_x=0.2)
                delete_button.bind(on_press=lambda btn, i=index: self.delete_schedule(i))
                detail_layout.add_widget(delete_button)

                self.layout.add_widget(detail_layout)
        else:
            self.layout.add_widget(Label(text="指定した日付に予定はありません"))

    def delete_schedule(self, index):
        display_screen = self.manager.get_screen('display')
        if self.current_date in display_screen.schedule_data:
            del display_screen.schedule_data[self.current_date][index]
            if not display_screen.schedule_data[self.current_date]:  # If no schedules remain for that date
                del display_screen.schedule_data[self.current_date]
            display_screen.save_to_csv()
            self.show_details(self.current_date)

class ScheduleApp(App):    
    def build(self):
        sm = ScreenManager()
        display_screen = DisplayScreen(name='display')
        sm.add_widget(RegistrationScreen(name='register'))
        sm.add_widget(display_screen)
        sm.add_widget(DetailsScreen(name='details'))
        display_screen.load_from_csv()  # アプリを起動するときにCSVから予定を読み込む
        return sm

if __name__ == "__main__":
    ScheduleApp().run()
