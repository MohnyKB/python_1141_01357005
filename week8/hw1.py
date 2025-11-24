import tkinter as tk

def calculate():
    score = 0

    if q1.get() == 1:
        score += 1
    if q2.get() == 1:
        score += 1
    if q3.get() == 1:
        score += 1
    if q4.get() == 1:
        score += 1

    if score>=3:
        status = "健康狀況良好"
    else:
        status = "健康狀況不好"
    
    score_label.config(text=f"您的總分為:{score}")
    status_label.config(text=f"健康狀況:{status}")

root = tk.Tk()
root.title("生活健康狀況問卷")
root.geometry("500x450")
title_label = tk.Label(root, text="生活健康狀況問卷", font=(20))
title_label.pack(pady=20)

q1 = tk.IntVar()
q2 = tk.IntVar()
q3 = tk.IntVar()
q4 = tk.IntVar()

f1 = tk.Frame(root)
f1.pack(fill="x", padx=50, pady=5)
tk.Label(f1, text="1.請問是否有抽菸習慣?").pack(side="left")
tk.Radiobutton(f1, text="否", variable=q1, value=1).pack(side="right")
tk.Radiobutton(f1, text="是", variable=q1, value=0).pack(side="right")


f2 = tk.Frame(root)
f2.pack(fill="x", padx=50, pady=5)
tk.Label(f2, text="2.請問是否有飲酒習慣?").pack(side="left")
tk.Radiobutton(f2, text="否", variable=q2, value=1).pack(side="right")
tk.Radiobutton(f2, text="是", variable=q2, value=0).pack(side="right")


f3 = tk.Frame(root)
f3.pack(fill="x", padx=50, pady=5)
tk.Label(f3, text="3.每天睡眠時間是否超過六小時?").pack(side="left")
tk.Radiobutton(f3, text="否", variable=q3, value=0).pack(side="right")
tk.Radiobutton(f3, text="是", variable=q3, value=1).pack(side="right")


f4 = tk.Frame(root)
f4.pack(fill="x", padx=50, pady=5)
tk.Label(f4, text="4.是否有均衡飲食?").pack(side="left")
tk.Radiobutton(f4, text="否", variable=q4, value=0).pack(side="right")
tk.Radiobutton(f4, text="是", variable=q4, value=1).pack(side="right")


btn = tk.Button(root, text="送出問卷並顯示結果", command=calculate)
btn.pack(pady=30)

score_label = tk.Label(root, text="")
score_label.pack()
status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()