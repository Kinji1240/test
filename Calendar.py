import tkinter as tk
from tkcalendar import Calendar  # プロジェクトに tkcalendar モジュールをインストール

def save_event():
    date = cal.get_date()
    event = event_entry.get()
    if date and event:
        with open("calendar.txt", "a") as file:
            file.write(f"{date}: {event}\n")
        event_entry.delete(0, "end")

def show_events():
    with open("calendar.txt", "r") as file:
        events = file.readlines()
    event_text.config(state="normal")
    event_text.delete("1.0", "end")
    for event in events:
        event_text.insert("end", event)
    event_text.config(state="disabled")

# Tkinterウィンドウを作成
window = tk.Tk()
window.title("カレンダーアプリ")

# カレンダーウィジェットを作成
cal = Calendar(window)
cal.pack(pady=10)

# 予定の入力フィールド
event_label = tk.Label(window, text="予定:")
event_label.pack()
event_entry = tk.Entry(window)
event_entry.pack()

# 予定を保存するボタン
save_button = tk.Button(window, text="予定を保存", command=save_event)
save_button.pack()

# 予定を表示するテキストボックス
event_text = tk.Text(window, height=10, width=40)
event_text.pack()

# 予定を表示するボタン
show_button = tk.Button(window, text="予定を表示", command=show_events)
show_button.pack()

# ウィンドウを表示
window.mainloop()