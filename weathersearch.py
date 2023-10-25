import tkinter as tk
from tkinter import ttk
import csv
import time

# CSVファイルから情報を読み込む関数
def read_csv(file_path):
    data = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # ヘッダー行を取得
        for row in csv_reader:
            prefecture = row[0]
            data[prefecture] = row
    return data, header

# 都道府県が選択されたときに情報を表示する関数
def display_info():
    selected_prefecture = prefecture_var.get()
    if selected_prefecture in data:
        info = data[selected_prefecture]
        info_text.config(state="normal")
        info_text.delete("1.0", "end")
        info_text.insert("end", "\n".join(info))
        info_text.config(state="disabled")
    else:
        info_text.config(state="normal")
        info_text.delete("1.0", "end")
        info_text.insert("end", "選択した都道府県の情報はありません。")
        info_text.config(state="disabled")

# 自動更新関数
def auto_update():
    display_info()
    window.after(3600000, auto_update)  # 1時間ごとに更新 (1時間 = 3600000ミリ秒)

# Tkinterウィンドウを作成
window = tk.Tk()
window.title("天気情報")

# CSVファイルのパス
csv_file_path = "weather_report.csv"

# CSVファイルから情報を読み込み
data, header = read_csv(csv_file_path)

# 都道府県の選択メニュー
prefecture_var = tk.StringVar()
prefecture_label = tk.Label(window, text="都道府県:")
prefecture_label.pack()
prefecture_combobox = ttk.Combobox(window, textvariable=prefecture_var, values=list(data.keys()))
prefecture_combobox.pack()
prefecture_combobox.bind("<<ComboboxSelected>>", lambda event: display_info())

# 都道府県の情報表示
info_text = tk.Text(window, height=10, width=40)
info_text.pack()

# 自動更新を開始
auto_update()

# ウィンドウを表示
window.mainloop()