import tkinter as tk
import csv

# CSVファイルから情報を読み込む関数
def read_csv(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # ヘッダー行をスキップ
        for row in csv_reader:
            data.append(row)
    return data

# Tkinterウィンドウを作成
window = tk.Tk()
window.title("天気情報")

# CSVファイルのパス
csv_file_path = "weather_report.csv"

# CSVファイルから情報を読み込み
data = read_csv(csv_file_path)

# ラベルを作成して情報を表示
for row_idx, row_data in enumerate(data):
    for col_idx, cell_data in enumerate(row_data):
        label = tk.Label(window, text=cell_data, borderwidth=1, relief="solid")
        label.grid(row=row_idx, column=col_idx, padx=5, pady=5)

# ウィンドウを表示
window.mainloop()