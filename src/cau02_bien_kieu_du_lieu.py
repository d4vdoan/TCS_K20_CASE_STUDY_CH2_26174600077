# 1. Tạo biến theo quy tắc snake_case, chọn kiểu dữ liệu phù hợp
ma_phien = "LAB026"        # str
ma_may = "PC12"            # str
cong_suat = 250.0          # float (W)
thoi_gian = 90             # int (phút)
dang_hoat_dong = True      # bool
ghi_chu = None             # NoneType (chưa có ghi chú)

# 2. In từng giá trị và kiểm tra kiểu bằng type()
print(ma_phien, type(ma_phien))
print(ma_may, type(ma_may))
print(cong_suat, type(cong_suat))
print(thoi_gian, type(thoi_gian))
print(dang_hoat_dong, type(dang_hoat_dong))
print(ghi_chu, type(ghi_chu))

# 3. Gán lại thời gian từ 90 thành 120 rồi in giá trị mới
thoi_gian = 120
print("Thời gian mới:", thoi_gian, type(thoi_gian))