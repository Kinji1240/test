from tkinter import *
import time
import math

WINwidth = 400  # ウィンドウの幅を小さく調整

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

# 各針の色を設定
H_color_index = 0  # 長針の色のインデックス
M_color_index = 1  # 短針の色のインデックス
S_color_index = 6  # 秒針の色のインデックス

# 数字の色を変更する関数
def change_needle_color(needle, new_color):
    global color_index
    color_index = rainbow_colors.index(new_color)

    # 長針、短針、秒針の色をそれぞれ設定
    if needle == 0:
        global H_color_index
        H_color_index = color_index
    elif needle == 1:
        global M_color_index
        M_color_index = color_index
    elif needle == 2:
        global S_color_index
        S_color_index = color_index

    update_button_states(needle)

def update_button_states(needle):
    for button in color_buttons[needle]:
        if button["text"] == rainbow_colors[color_index]:
            button["state"] = "disabled"
        else:
            button["state"] = "active"

def draw_clock():
    global w  # グローバルの w キャンバスを使用
    w.delete(ALL)  # キャンバス内のすべての要素をクリア

    # 描画の処理はここに入れる
    # 以下、サンプルのコードをそのまま記述

    now = time.localtime()
    if now.tm_hour > 12:
        nowhour = now.tm_hour - 12
    else:
        nowhour = now.tm_hour

    nowhour = nowhour + now.tm_min / 60 + now.tm_sec / 3600
    nowminute = now.tm_min + now.tm_sec / 60

    H_A = nowhour / 12 * 360 * math.pi / 180
    M_A = nowminute / 60 * 360 * math.pi / 180
    S_A = now.tm_sec / 60 * 360 * math.pi / 180

    H_x = math.cos(H_A) * H_length
    H_y = math.sin(H_A) * H_length
    M_x = math.cos(M_A) * M_length
    M_y = math.sin(M_A) * M_length
    S_x = math.cos(S_A) * S_length
    S_y = math.sin(S_A) * S_length

    w.create_oval(WINwidth / 2 - 5, WINheight / 2 - 5, WINwidth / 2 + 5, WINheight / 2 + 5, fill="black")
    w.create_oval(5, 5, WINwidth - 5, WINheight - 5, width=2)
    
    w.create_line(WINwidth / 2, WINheight / 2, WINwidth / 2 + H_y, WINheight / 2 - H_x, width=H_LINEwidth, fill=rainbow_colors[H_color_index])  # 時針
    w.create_line(WINwidth / 2, WINheight / 2, WINwidth / 2 + M_y, WINheight / 2 - M_x, width=M_LINEwidth, fill=rainbow_colors[M_color_index])  # 分針
    w.create_line(WINwidth / 2, WINheight / 2, WINwidth / 2 + S_y, WINheight / 2 - S_x, width=S_LINEwidth, fill=rainbow_colors[S_color_index])  # 秒針

    w.update()

# Tk() インスタンスを作成
Clock = Tk()
Clock.title("AnalogClock")

# Canvas を作成
w = Canvas(Clock, width=WINwidth, height=WINheight, background="black")  # 背景色を黒色に変更
w.pack()

# 数字の色変更ボタンを追加
color_buttons = [[] for _ in range(3)]
for needle, color_index in enumerate([H_color_index, M_color_index, S_color_index]):
    for i, color in enumerate(rainbow_colors):
        color_button = Button(Clock, text=color, command=lambda needle=needle, color=color: change_needle_color(needle, color))
        color_button.pack(side=LEFT, padx=5)
        color_buttons[needle].append(color_button)

update_button_states(0)
update_button_states(1)
update_button_states(2)

try:
    while True:
        # ここから無限ループ
        draw_clock()
        time.sleep(0.1)
except:
    pass

Clock.mainloop()  # Tkinter アプリケーションループを開始