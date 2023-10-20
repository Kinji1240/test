from tkinter import *
from datetime import datetime
import time
import math

WINwidth = 800

# 背景色の一覧を定義（虹色）
rainbow_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
color_index = 0  # 色のインデックス

WINheight = WINwidth
S_length = WINwidth / 2 * 0.75
M_length = S_length * 0.95
H_length = S_length * 0.8
H_LINEwidth = 8
M_LINEwidth = H_LINEwidth / 2
S_LINEwidth = 1

# FontSize をグローバルスコープで定義
FontSize = int(WINwidth / 14)

# 数字の色を変更する関数
def change_number_color(new_color):
    global color_index
    color_index = rainbow_colors.index(new_color)
    w.itemconfig(time_text, fill=new_color)
    update_button_states()

def update_button_states():
    for button in color_buttons:
        if button["text"] == rainbow_colors[color_index]:
            button["state"] = "disabled"
        else:
            button["state"] = "active"

def draw_clock():
    global w  # グローバルの w キャンバスを使用
    w.delete(ALL)  # キャンバス内のすべての要素をクリア

    # 描画の処理はここに入れる
    # 以下、サンプルのコードをそのまま記述

    now = datetime.now()
    if now.hour > 12:
        nowhour = now.hour - 12
    else:
        nowhour = now.hour

    nowhour = nowhour + now.minute / 60 + now.second / 3600
    nowminute = now.minute + now.second / 60

    H_A = nowhour / 12 * 360 * math.pi / 180
    M_A = nowminute / 60 * 360 * math.pi / 180
    S_A = now.second / 60 * 360 * math.pi / 180

    H_x = math.cos(H_A) * H_length
    H_y = math.sin(H_A) * H_length
    M_x = math.cos(M_A) * M_length
    M_y = math.sin(M_A) * M_length
    S_x = math.cos(S_A) * S_length
    S_y = math.sin(S_A) * S_length

    global time_text
    time_text = w.create_text(WINwidth / 2, WINheight / 2 + WINwidth / 8, text=datetime.now().strftime('%Y/%m/%d %H:%M:%S'), font=("", int(FontSize / 1.5), "bold"), fill=rainbow_colors[color_index])  # 年月日時分秒

    w.create_oval(WINwidth / 2 - 5, WINheight / 2 - 5, WINwidth / 2 + 5, WINheight / 2 + 5, fill="black")
    w.create_oval(5, 5, WINwidth - 5, WINheight - 5, width=2)
    
    w.create_line(WINwidth / 2, WINheight / 2, WINwidth / 2 + H_y, WINheight / 2 - H_x, width=H_LINEwidth, fill="white")  # 時針
    w.create_line(WINwidth / 2, WINheight / 2, WINwidth / 2 + M_y, WINheight / 2 - M_x, width=M_LINEwidth, fill="white")  # 分針
    w.create_line(WINwidth / 2, WINheight / 2, WINwidth / 2 + S_y, WINheight / 2 - S_x, width=S_LINEwidth, fill="lightblue")  # 秒針（水色）

    w.update()

# Tk() インスタンスを作成
Clock = Tk()
Clock.title("AnalogClock")

# Canvas を作成
w = Canvas(Clock, width=WINwidth, height=WINheight, background="black")  # 背景色を黒色に変更
w.pack()

# 数字の色変更ボタンを追加
color_buttons = []
for i, color in enumerate(rainbow_colors):
    color_button = Button(Clock, text=color, command=lambda color=color: change_number_color(color))
    color_button.pack(side=LEFT, padx=5)
    color_buttons.append(color_button)

update_button_states()

try:
    while True:
        # ここから無限ループ
        draw_clock()
        time.sleep(0.1)
except:
    pass

Clock.mainloop()  # Tkinter アプリケーションループを開始