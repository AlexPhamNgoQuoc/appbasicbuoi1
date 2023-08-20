import tkinter as tk
from tkinter import ttk

def tinh_toan():
    d = float(dai.get())
    r = float(rong.get())
    
    chu_vi = 2 * (d + r)
    dien_tich = d * r
    
    ket_qua.config(text=f"Chu vi: {chu_vi}\nDiện tích: {dien_tich}")

# Tạo cửa sổ giao diện
root = tk.Tk()
root.title("Tính chu vi và diện tích hình chữ nhật")

# Đặt kích thước cửa sổ
root.geometry("400x300")

# Tạo style tùy chỉnh cho giao diện
style = ttk.Style()
style.configure("Custom.TLabel", font=("Arial", 12))
style.configure("Custom.TEntry", font=("Arial", 12))

# Tạo các widgets
label_dai = ttk.Label(root, text="Độ dài:", style="Custom.TLabel")
dai = ttk.Entry(root, style="Custom.TEntry")

label_rong = ttk.Label(root, text="Chiều rộng:", style="Custom.TLabel")
rong = ttk.Entry(root, style="Custom.TEntry")

nut_tinh = ttk.Button(root, text="Tính", command=tinh_toan)

ket_qua = ttk.Label(root, text="", justify="left", style="Custom.TLabel")

# Hiển thị các widgets sử dụng grid layout
label_dai.grid(row=0, column=0)
dai.grid(row=0, column=1)

label_rong.grid(row=1, column=0)
rong.grid(row=1, column=1)

nut_tinh.grid(row=2, columnspan=2)

ket_qua.grid(row=3, columnspan=2)

# Khởi chạy giao diện
root.mainloop()
