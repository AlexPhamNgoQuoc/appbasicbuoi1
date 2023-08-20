def tinh_toan(a, b):
    try:
        gia_tri_a = float(a)
        gia_tri_b = float(b)
        
        ket_qua_tong = gia_tri_a + gia_tri_b
        ket_qua_hieu = gia_tri_a - gia_tri_b
        ket_qua_tich = gia_tri_a * gia_tri_b

        if gia_tri_b != 0:
            ket_qua_thuong = gia_tri_a / gia_tri_b
        else:
            ket_qua_thuong = "Không thể tính thương vì b = 0"
        
        return ket_qua_tong, ket_qua_hieu, ket_qua_tich, ket_qua_thuong
    except ValueError:
        return "Đầu vào không hợp lệ. Vui lòng nhập số hợp lệ."

# Nhập giá trị của a và b
a_input = input("Nhập giá trị của a: ")
b_input = input("Nhập giá trị của b: ")

# Tính toán kết quả
ket_qua_tong, ket_qua_hieu, ket_qua_tich, ket_qua_thuong = tinh_toan(a_input, b_input)

# Hiển thị kết quả
print("Tổng của a và b:", ket_qua_tong)
print("Hiệu của a và b:", ket_qua_hieu)
print("Tích của a và b:", ket_qua_tich)
print("Thương của a và b:", ket_qua_thuong)
