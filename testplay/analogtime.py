from tkinter import *
from datetime import datetime
import math

WINwidth = 800
WINcolor1 = 'white'  
WINcolor2 = 'black'

# 以前のコードと同じです

def switch_background_color():
    global bg_color
    if bg_color == WINcolor1:
        bg_color = WINcolor2
    else:
        bg_color = WINcolor1
    draw_clock()

def draw_clock():
    global w
    w.delete(ALL)

    # 以前のコードと同じです

    # 数字を描画（背景色に合わせて切り替え）
    if bg_color == WINcolor1:
        font_color = 'black'
    else:
        font_color = 'white'
    
    Fx = 0
    Fy = FontSize / 10
    R = S_length + FontSize * 0.9
    A = 0
    for i in range(1, 13):
        A = A + 30
        Tx = R * math.cos(A / 180 * math.pi)
        Ty = R * math.sin(A / 180 * math.pi)
        w.create_text(WINwidth / 2 + Ty - Fx, WINheight / 2 - Tx + Fy, text=i, font=("", FontSize, "bold"), fill=font_color)

    w.configure(background=bg_color)

Clock = Tk()
Clock.title("AnalogClock")

w = Canvas(Clock, width=WINwidth, height=WINheight, background=bg_color)
w.pack()

bg_color = WINcolor1

button = Button(Clock, text="Change Background", command=switch_background_color)
button.pack(pady=10)

draw_clock()

Clock.mainloop()
