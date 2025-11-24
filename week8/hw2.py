import tkinter as tk

total_amount = 0.0

def add_item():
    global total_amount

    item_name = entry_item.get()
    item_price_str = entry_price.get()
    
    if item_name == "" or item_price_str == "":
        return
    
    price = float(item_price_str)
    
    total_amount += price
    update_total_label()
    
    display_text = f"{item_name} - {price:.2f} 元"
    listbox.insert(tk.END, display_text)
    
    entry_item.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    
def delete_selected():
    global total_amount

    selection = listbox.curselection()
    if not selection:
        return
    
    index = selection[0]
    text = listbox.get(index)
    
    price_part = text.split(" - ")[1].replace(" 元", "")
    price = float(price_part)
    
    total_amount -= price
    update_total_label()
    
    listbox.delete(index)
    
def update_total_label():
    label_total.config(text=f"總金額： {total_amount:.2f} 元")
   
def clear_all():
    global total_amount

    listbox.delete(0, tk.END)
    total_amount = 0.0
    update_total_label()
    
root = tk.Tk()
root.title("記帳小工具")
root.geometry("400x350")

top_frame = tk.Frame(root)
top_frame.pack(pady=10)

input_frame = tk.Frame(top_frame)
input_frame.pack(side="left",padx=10)

tk.Label(input_frame, text="品項:").grid(row=0, column=0, pady=5)
entry_item = tk.Entry(input_frame)
entry_item.grid(row=0, column=1, pady=5)

tk.Label(input_frame, text="金額 :").grid(row=1, column=0, pady=5)
entry_price = tk.Entry(input_frame)
entry_price.grid(row=1, column=1, pady=5)

btn_frame = tk.Frame(top_frame)
btn_frame.pack(side="right", padx=10)

btn_add = tk.Button(btn_frame, text="新增", width=8, command=add_item)
btn_add.pack(pady=5)

btn_del = tk.Button(btn_frame, text="刪除選取", width=8, command=delete_selected)
btn_del.pack(pady=5)

listbox = tk.Listbox(root, width=40, height=8)
listbox.pack(padx=20, pady=5)

btn_clear = tk.Button(root, text="清空", width=8, command=clear_all)
btn_clear.pack(anchor="e", padx=40, pady=5)

label_total = tk.Label(root, text="總金額： 0.00 元", font=("Arial",12, "bold"))
label_total.pack(anchor="w", padx=20, pady=10)

root.mainloop()