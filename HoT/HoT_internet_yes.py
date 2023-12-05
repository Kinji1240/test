import tkinter as tk

def connect_to_wifi():
    ssid = entry_ssid.get()
    password = entry_password.get()
    
    # ここで Wi-Fi 接続の処理を行う（実際の処理はOSやライブラリに依存）

    result_label.config(text=f"Wi-Fiに接続しました。\nSSID: {ssid}\nPassword: {password}")

# GUIの作成
app = tk.Tk()
app.title("Wi-Fi接続画面")

# Wi-Fi設定入力欄
label_ssid = tk.Label(app, text="Wi-Fi SSID:")
label_ssid.grid(row=0, column=0, padx=10, pady=10)
entry_ssid = tk.Entry(app)
entry_ssid.grid(row=0, column=1, padx=10, pady=10)

label_password = tk.Label(app, text="Wi-Fi Password:")
label_password.grid(row=1, column=0, padx=10, pady=10)
entry_password = tk.Entry(app, show="*")  # パスワードは * で表示
entry_password.grid(row=1, column=1, padx=10, pady=10)

# 接続ボタン
connect_button = tk.Button(app, text="接続", command=connect_to_wifi)
connect_button.grid(row=2, column=0, columnspan=2, pady=20)

# 結果表示ラベル
result_label = tk.Label(app, text="", font=("Helvetica", 12))
result_label.grid(row=3, column=0, columnspan=2, pady=10)

app.mainloop()
