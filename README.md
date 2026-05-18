# Digital_time-py
## デジタル時計で単純なやつです
- 練習になるところです↓
```py
import time

def update_time():
    #現在の時刻取得
    current_time = time.strftime("%H: %M: %S")
    # ラベル
    label.config(text=current_time)

    root.after(1000, update_time)
```
- ぜひ試してください
