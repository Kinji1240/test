import datetime
import googleapiclient.discovery
import google.auth

# ① Google APIの準備をする
SCOPES = ['https://www.googleapis.com/auth/calendar']
calendar_id = 'j5gr4sa@gmail.com'

# Googleの認証情報をファイルから読み込む
gapi_creds = google.auth.load_credentials_from_file(
    'C:/Users/204014/git_test/j5g-p-403802-f6d11f806041.json',
    SCOPES
)[0]

# APIと対話するためのResourceオブジェクトを構築する
service = googleapiclient.discovery.build('calendar', 'v3', credentials=gapi_creds)

# ② 今日の日付を取得
today = datetime.date.today()
start_of_day = datetime.datetime(today.year, today.month, today.day, 0, 0, 0).isoformat() + 'Z'
end_of_day = datetime.datetime(today.year, today.month, today.day, 23, 59, 59).isoformat() + 'Z'

# ③ Googleカレンダーから1日のイベントを取得する
event_list = service.events().list(
    calendarId=calendar_id, timeMin=start_of_day, timeMax=end_of_day,
    maxResults=10, singleEvents=True,
    orderBy='startTime'
).execute()

# ④ イベントの開始時刻、終了時刻、概要を取得して出力する
events = event_list.get('items', [])
response = '[今日の予定]\n'

for event in events:
    start_time = event['start'].get('dateTime', event['start'].get('date'))
    end_time = event['end'].get('dateTime', event['end'].get('date'))
    summary = event['summary']

    # イベントが終日の場合
    if 'date' in start_time:
        response += f'{start_time}: {summary} (終日)\n'
    else:
        response += f'{start_time} ～ {end_time}: {summary}\n'

# 出力を表示
print(response)