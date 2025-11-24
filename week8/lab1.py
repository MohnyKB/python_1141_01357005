import tkinter as tk

root = tk.Tk()
root.title("BMI 計算機")
root.geometry("300x250")

def execute():
    h_cm = float(height.get())
    h_m = h_cm / 100

    w_kg = float(weight.get())
    BMIval = w_kg / (h_m * h_m) 

    BMItext.config(text = f"您的 BMI : {BMIval:.2f}")

    BMIbot = 18.5 * (h_m * h_m)
    BMItop = 24 * (h_m * h_m)

    BMItext2.config(text = f"健康體重範圍 : {BMIbot:.1f}kg ~ {BMItop:.1f}kg")


height = tk.Entry(master=root)
weight = tk.Entry(master=root)
height_label = tk.Label(master=root, text="身高 (公分) :")
weight_label = tk.Label(master=root, text="體重 (公斤) :")

BMItext =  tk.Label(master=root, text="")
BMItext2 =  tk.Label(master=root, text="")

count = tk.Button(master=root, text="計算 BMI", command=execute)



height_label.grid(row=0, column=0, padx=5, sticky='w') 
height.grid(row=0, column=1, padx=5)
weight_label.grid(row=1, column=0, padx=5, sticky='w')
weight.grid(row=1, column=1, padx=5)
count.grid(row=2, column=0, columnspan=2)

BMItext.grid(row=3, column=0, columnspan=2, sticky='w')
BMItext2.grid(row=4, column=0, columnspan=2, sticky='w')

root.mainloop()