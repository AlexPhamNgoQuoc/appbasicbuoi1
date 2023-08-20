import tkinter as tk
from tkinter import ttk

def calculate():
    d = float(entry_length.get())
    r = float(entry_width.get())
    
    chu_vi = 2 * (d + r)
    dien_tich = d * r
    
    result_label.config(text=f"Chu vi: {chu_vi}\nDiện tích: {dien_tich}")

# Tạo cửa sổ giao diện
root = tk.Tk()
root.title("Tính chu vi và diện tích hình chữ nhật")

# Đặt kích thước ban đầu cho cửa sổ (trở lại kích thước ban đầu)
root.geometry("300x200")  # Chỉnh kích thước cửa sổ thành 300x200

# Tạo style tùy chỉnh cho giao diện
style = ttk.Style()
style.configure("Custom.TLabel", font=("Arial", 12))  # Đặt font chữ và kích thước cho Label
style.configure("Custom.TEntry", font=("Arial", 12))  # Đặt font chữ và kích thước cho Entry

# Tạo các widgets
length_label = ttk.Label(root, text="Độ dài:", style="Custom.TLabel")
entry_length = ttk.Entry(root, style="Custom.TEntry")

width_label = ttk.Label(root, text="Chiều rộng:", style="Custom.TLabel")
entry_width = ttk.Entry(root, style="Custom.TEntry")

calculate_button = ttk.Button(root, text="Tính", command=calculate)

result_label = ttk.Label(root, text="", justify="left", style="Custom.TLabel")

# Hiển thị các widgets sử dụng grid layout
length_label.grid(row=0, column=0)
entry_length.grid(row=0, column=1)

width_label.grid(row=1, column=0)
entry_width.grid(row=1, column=1)

calculate_button.grid(row=2, columnspan=2)

result_label.grid(row=3, columnspan=2)

# Khởi chạy giao diện
root.mainloop()
