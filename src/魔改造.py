import time
import tkinter as tk

class UltraClock:
    def __init__(self, root):
        self.root = root
        
        # --- 安全設計: 右上の「×」でいつでも消せる！ ---
        self.root.title("ULTRA_FAST_CLOCK")
        self.root.geometry("450x140")
        self.root.config(bg="#050508")         # 漆黒の背景
        self.root.attributes("-topmost", True) # 常に最前面に表示
        
        # メイン時刻表示（AM/PM ＋ 時:分:秒）
        self.lbl_time = tk.Label(
            self.root, text="AM 00:00:00", 
            font=("Consolas", 42, "bold"), bg="#050508", fg="#00ffcc" # 鮮やかなシアン
        )
        self.lbl_time.pack(expand=True, pady=(10, 0))

        # サブ表示（日付 ＋ 超高速ミリ秒）
        self.lbl_sub = tk.Label(
            self.root, text="0000/00/00 MON .000", 
            font=("Consolas", 16, "bold"), bg="#050508", fg="#ff0055" # 映えるネオンピンク
        )
        self.lbl_sub.pack(pady=(0, 15))

        # 超高速ループ開始
        self.update_ultra_system()

    def update_ultra_system(self):
        # 現在時刻（エポックタイム）を取得してミリ秒を計算
        now = time.time()
        time_struct = time.localtime(now)
        ms = int((now - int(now)) * 1000) # 小数点以下をミリ秒に変換
        
        # フォーマット整形（%p で AM/PM を取得）
        str_time = time.strftime("%p %I:%M:%S", time_struct) # %I で12時間制（01〜12）に
        str_date = time.strftime("%Y/%m/%d %a", time_struct).upper()
        

        self.lbl_time.config(text=str_time)
        self.lbl_sub.config(text=f"{str_date} .{ms:03d}") # ミリ秒を3桁固定で結合
        
        self.root.after(20, self.update_ultra_system)

if __name__ == "__main__":
    root = tk.Tk()
    app = UltraClock(root)
    root.mainloop()
