import tkinter as tk
from tkinter import font
import csv

# フォント情報を保存するCSVファイル
csv_filename = "font_info.csv"

# 利用可能なフォントのリスト
available_fonts = [
    "C:/Users/204004/Desktop/font/Mystic Soul.ttf",
    "C:/Users/204004/Desktop/font/NikkyouSans-mLKax.ttf",
    "C:/Users/204004/Desktop/font/Togalite-Black.otf"
]

# フォント選択用のウィンドウを表示
font_selection_window = tk.Tk()
font_selection_window.title("フォント選択")

# フォント選択用のメッセージ
font_message = tk.Label(font_selection_window, text="フォントを選択してください")
font_message.pack()

# フォント選択用のドロップダウンリスト
font_var = tk.StringVar(font_selection_window)
font_var.set(available_fonts[0])  # 初期値を設定
font_dropdown = tk.OptionMenu(font_selection_window, font_var, *available_fonts)
font_dropdown.pack()

def save_font_info():
    # 選択されたフォント情報をCSVファイルに保存
    selected_font = font_var.get()
    with open(csv_filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Selected Font"])
        writer.writerow([selected_font])
    font_selection_window.destroy()

# 確定ボタン
confirm_button = tk.Button(font_selection_window, text="確定", command=save_font_info)
confirm_button.pack()

# ウィンドウを表示
font_selection_window.mainloop()