import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        a_value = float(a_entry.get())
        b_value = float(b_entry.get())
        
        sum_result.set(f"Tổng: {a_value + b_value}")
        difference_result.set(f"Hiệu: {a_value - b_value}")
        product_result.set(f"Tích: {a_value * b_value}")

        if b_value != 0:
            quotient_result.set(f"Thương: {a_value / b_value}")
        else:
            quotient_result.set("Không thể tính thương vì b = 0")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập đúng định dạng số.")

# Tạo giao diện đồ họa sử dụng tkinter
root = tk.Tk()
root.title("Chương trình tính toán")
root.geometry("400x300")

font = ("Arial", 16)

a_label = tk.Label(root, text="Nhập giá trị của a:", font=font)
a_label.pack()

a_entry = tk.Entry(root, font=font)
a_entry.pack()

b_label = tk.Label(root, text="Nhập giá trị của b:", font=font)
b_label.pack()

b_entry = tk.Entry(root, font=font)
b_entry.pack()

calculate_button = tk.Button(root, text="Tính toán", font=font, command=calculate)
calculate_button.pack()

sum_result = tk.StringVar()
difference_result = tk.StringVar()
product_result = tk.StringVar()
quotient_result = tk.StringVar()

sum_label = tk.Label(root, textvariable=sum_result, font=font)
sum_label.pack()

difference_label = tk.Label(root, textvariable=difference_result, font=font)
difference_label.pack()

product_label = tk.Label(root, textvariable=product_result, font=font)
product_label.pack()

quotient_label = tk.Label(root, textvariable=quotient_result, font=font)
quotient_label.pack()

root.mainloop()
