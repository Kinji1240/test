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

def switch_background_color():
    global color_index
    color_index = (color_index + 1) % len(rainbow_colors)
    bg_color = rainbow_colors[color_index]
    w.configure(background=bg_color)

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

    w.create_text(WINwidth / 2, WINheight / 2 + WINwidth / 8, text=datetime.now().strftime('%Y/%m/%d %H:%M:%S'), font=("", int(FontSize / 1.5), "bold"), fill="white")  # 年月日時分秒

    w.create_oval(WINwidth / 2 - 5, WINheight / 2 - 5, WINwidth / 2 + 5, WINheight / 2 + 5, fill="black")
    w.create_oval(5, 5, WINwidth - 5, WINheight - 5, width=2)
    
    w.create_line(WINwidth / 2, WINheight / 2, WINwidth / 2 + H_y, WINheight / 2 - H_x, width=H_LINEwidth, fill="white")  # 時針
    w.create_line(WINwidth / 2, WINheight / 2, WINwidth / 2 + M_y, WINheight / 2 - M_x, width=M_LINEwidth, fill="white")  # 分針
    w.create_line(WINwidth / 2, WINheight / 2, WINwidth / 2 + S_y, WINheight / 2 - S_x, width=S_LINEwidth, fill="red")  # 秒針

    w.update()

# Tk() インスタンスを作成
Clock = Tk()
Clock.title("AnalogClock")

# Canvas を作成
w = Canvas(Clock, width=WINwidth, height=WINheight, background=rainbow_colors[color_index])
w.pack()

# 背景色切り替えボタンを追加
button = Button(Clock, text="Change Background", command=switch_background_color)
button.pack(pady=10)

try:
    while True:
        # ここから無限ループ
        draw_clock()
        time.sleep(0.1)
except:
    pass

Clock.mainloop()  # Tkinter アプリケーションループを開始