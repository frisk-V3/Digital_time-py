import tkinter as tk
import time

def update_time():
    #現在の時刻取得
    current_time = time.strftime("%H: %M: %S")
    # ラベル
    label.config(text=current_time)

    root.after(1000, update_time)

#メインウィンドウ
root = tk.Tk()
root.title("デジタル時計")
root.geometry("300x150")

label = tk.Label(root, font=("Helvetica", 48), bg="black", fg="cyan")
label.pack(expand=True, fill="both")

#時間を更新
update_time()

#画面を動かし続ける
root.mainloop() # コレがないと一瞬で消える
