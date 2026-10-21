ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất W: "))
so_phut = int(input("Nhập số phút: "))

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")

# Lỗi 1 (dòng 5, TypeError): input() trả về str nên cong_suat_w là chuỗi, không chia được; đã sửa bằng float().
# Lỗi 2 (dòng 7, NameError): trong f-string gõ sai tên biến dien_nang, đúng phải là dien_nang_kwh.