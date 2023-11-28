from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from googleapiclient.discovery import build
from google.auth import load_credentials_from_file
import datetime
import japanize_kivy

class CalendarApp(App):
    def build(self):
        # Kivyウィジェットの作成
        self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text='一日の予定:', font_size='20sp')  # フォントサイズを大きく設定
        self.layout.add_widget(self.label)

        # Google Calendar APIの準備
        self.SCOPES = ['https://www.googleapis.com/auth/calendar']
        self.calendar_id = 'j5gr4sa@gmail.com'
        self.gapi_creds = load_credentials_from_file(
            'j5g-p-403802-f6d11f806041.json',
            self.SCOPES
        )
        self.service = build('calendar', 'v3', credentials=self.gapi_creds[0])

        # 初回更新を実行
        self.update_schedule()

        # 1秒ごとにupdate_scheduleメソッドを呼び出す
        Clock.schedule_interval(self.update_schedule, 1)

        return self.layout

    def update_schedule(self, dt=None):
        # 今日の日付を取得
        today = datetime.date.today()
        start_of_day = datetime.datetime(today.year, today.month, today.day, 0, 0, 0).isoformat() + 'Z'
        end_of_day = datetime.datetime(today.year, today.month, today.day, 23, 59, 59).isoformat() + 'Z'

        # Googleカレンダーから1日のイベントを取得
        event_list = self.service.events().list(
            calendarId=self.calendar_id, timeMin=start_of_day, timeMax=end_of_day,
            maxResults=10, singleEvents=True,
            orderBy='startTime'
        ).execute()

        # イベントの開始時刻、終了時刻、概要を取得して出力する
        events = event_list.get('items', [])

        # イベントが存在する場合にスケジュールを構築
        if events:
            schedule = "[今日の予定]\n"

            for event in events:
                start_time = event['start'].get('dateTime', event['start'].get('date'))
                end_time = event['end'].get('dateTime', event['end'].get('date'))
                summary = event.get('summary', 'No summary')

                # イベントが終日の場合
                if 'date' in start_time:
                    schedule += f'{start_time}: {summary} (終日)\n'
                else:
                    schedule += f'{start_time} ～ {end_time}: {summary}\n'
        else:
            schedule = "[今日の予定はありません]\n"

        # 予定を更新
        self.label.text = schedule

if __name__ == '__main__':
    CalendarApp().run()
