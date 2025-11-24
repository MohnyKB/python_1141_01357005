import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("貨幣兌換小工具")
root.geometry("400x300")

currency_options = ["TWD", "USD", "JPY", "EUR"]

def execute():
    try:
        val = float(value.get())
        place_str = origin.get() 
        target_str = target.get()

        if not place_str or not target_str:
            outcome.config(text="請選擇貨幣")
            return

        temp = 0
        if place_str == "TWD":
            temp = val * 1
        elif place_str == "USD":
            temp = val * 31
        elif place_str == "JPY":
            temp = val * 0.22
        elif place_str == "EUR":
            temp = val * 34

        result = 0
        if target_str == "TWD":
            result = temp / 1
        elif target_str == "USD":
            result = temp / 31
        elif target_str == "JPY":
            result = temp / 0.22
        elif target_str == "EUR":
            result = temp / 34
        
        outcome.config(text = f"結果: {val:.2f} {place_str} = {result:.2f} {target_str}")
        
    except ValueError:
        outcome.config(text="錯誤：金額必須是數字")
    except Exception as e:
        outcome.config(text=f"發生錯誤: {e}")


value = tk.Entry(master=root)
value_label = tk.Label(master=root, text="金額: ")

origin = ttk.Combobox(master=root, values=currency_options, state="readonly")
origin_label = tk.Label(master=root, text="原始貨幣: ")

target = ttk.Combobox(master=root, values=currency_options, state="readonly")
target_label = tk.Label(master=root, text="目標貨幣: ")

outcome =  tk.Label(master=root, text="")
count = tk.Button(master=root, text="開始換算", command=execute)

value_label.grid(row=0, column=0, padx=5, pady=5, sticky='w') 
value.grid(row=0, column=1, padx=5, pady=5) 

origin_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')
origin.grid(row=1, column=1, padx=5, pady=5)


target_label.grid(row=2, column=0, padx=5, pady=5, sticky='w')
target.grid(row=2, column=1, padx=5, pady=5)

count.grid(row=3, column=0, columnspan=2, pady=10)
outcome.grid(row=4, column=0, columnspan=2)

root.mainloop()