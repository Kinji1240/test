from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivycalendar import DatePicker

class EditableCalendarApp(App):
    def build(self):
        self.notes = {}  # 日付とメモの辞書

        layout = BoxLayout(orientation='vertical')

        # カレンダーウィジェットを作成
        self.calendar = DatePicker()
        self.calendar.bind(on_date=self.on_date_selected)
        layout.add_widget(self.calendar)

        # メモ表示用のラベル
        self.memo_label = Label(text='メモ:')
        layout.add_widget(self.memo_label)

        # メモ入力用のテキストボックス
        self.memo_input = Label()
        layout.add_widget(self.memo_input)

        return layout

    def on_date_selected(self, instance, value):
        selected_date = value
        memo = self.notes.get(selected_date, '')
        self.memo_input.text = memo
        self.memo_label.text = f'メモ ({selected_date}):'

if __name__ == '__main__':
    EditableCalendarApp().run()