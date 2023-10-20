#!/usr/bin/python3

from tkinter import *  #Window表示
from datetime import datetime  #日時を取得

import time  #sleepで0.1秒毎に表示を切り替える
import math  #三角関数・円周率

WINwidth = 800  #時計の大きさ（min=200:変更箇所はここだけ）
WINcolor = '#ffffff'  #BackGroundColor

WINheight = WINwidth  #Windowの高さ
S_length = WINwidth / 2 * 0.75  #秒針長さ
M_length = S_length * 0.95  #分針長さ
H_length = S_length * 0.8  #時針長さ
H_LINEwidth = 8  #時針の太さ
M_LINEwidth = H_LINEwidth / 2  #分針の太さ
S_LINEwidth = 1  #秒針の太さ

#Windowを作成
Clock = Tk()
Clock.title("AnalogClock")

w = Canvas(Clock, width = WINwidth, height = WINheight, background = WINcolor)
w.pack()

w.create_oval(WINwidth / 2 - 5, WINheight / 2 - 5, WINwidth / 2 + 5, WINheight / 2 + 5, fill="black")  #中心●
w.create_oval(5, 5, WINwidth-5, WINheight-5, width = 2)  #時計の外形円

FontSize = int(WINwidth / 14)  #時間文字のサイズ
Fx = 0  #時間文字の位置を修正
Fy = FontSize / 10
R = S_length + FontSize * 0.9  #時間文字位置の半径
A = 0  #時間文字位置の角度
for i in range(1,13):  #文字盤表示
    A = A + 30
    Tx = R * math.cos(A / 180 * math.pi)  #時間文字の座標
    Ty = R * math.sin(A / 180 * math.pi)
    w.create_text(WINwidth / 2 + Ty - Fx, WINheight / 2 - Tx + Fy, text = i, font = ("", FontSize))

try:
    while True:
        #ここから無限ループ
        now = datetime.now()  #現在の時間を取得
        if now.hour > 12:  #12時間表示
            nowhour = now.hour - 12
        else:
            nowhour = now.hour
        #秒針が動くと時分針も動かす
        nowhour = nowhour + now.minute / 60 + now.second / 3600  #時間を時に変換：例．1時30分30秒ー＞1.5083・・・
        nowminute = now.minute + now.second / 60  #分秒を分に変換

        H_A = nowhour / 12 * 360 * math.pi /180  #針の角度
        M_A = nowminute / 60 * 360 * math.pi / 180
        S_A = now.second / 60 * 360 * math.pi / 180

        H_x = math.cos(H_A) * H_length  #針の先端の座標計算（中心基準）
        H_y = math.sin(H_A) * H_length
        M_x = math.cos(M_A) * M_length
        M_y = math.sin(M_A) * M_length
        S_x = math.cos(S_A) * S_length
        S_y = math.sin(S_A) * S_length

        w.create_text(WINwidth / 2 , WINheight / 2 + WINwidth / 8, text = datetime.now().strftime('%Y/%m/%d %H:%M:%S'), font = ("", int(FontSize / 1.5)), tag="Y")  #年月日時分秒

        w.create_line(WINwidth / 2, WINheight / 2, WINwidth / 2 + H_y, WINheight / 2 - H_x, width = H_LINEwidth, tag="H") #時針
        w.create_line(WINwidth / 2, WINheight / 2, WINwidth / 2 + M_y, WINheight / 2 - M_x, width = M_LINEwidth, tag="M") #分針
        w.create_line(WINwidth / 2, WINheight / 2, WINwidth / 2 + S_y, WINheight / 2 - S_x, width = S_LINEwidth, tag="S") #秒針

        w.update()  #新しい針とカレンダーを表示

        w.delete("H")  #針とカレンダーを消去
        w.delete("M")
        w.delete("S")
        w.delete("Y")

        time.sleep(0.1)  #0.1秒毎に描画
except:

    pass
