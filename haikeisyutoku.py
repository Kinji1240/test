import csv
import tkinter as tk

# CSVファイルを読み込む
with open("color_settings.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # ヘッダ行をスキップ

    # 2列目の情報を取得
    for row in reader:
        try:
            green_value = float(row[1])
            break  # 最初の行の値を使用
        except ValueError:
            pass

# 色を計算
color = (0, int(green_value * 255), 0)

# 色を16進数に変換
hex_color = '#{:02x}{:02x}{:02x}'.format(*color)

# ウィンドウを作成
root = tk.Tk()
root.title("背景色とウィジェット")

# 背景色を設定
root.configure(bg=hex_color)

# ウィジェットを作成して配置
label = tk.Label(root, text="このウィジェットの背景色", bg=hex_color)
label.pack(padx=20, pady=20)

root.mainloop()