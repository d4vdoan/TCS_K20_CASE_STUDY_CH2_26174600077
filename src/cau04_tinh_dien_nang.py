cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000

# 13. Tính điện năng tiêu thụ và chi phí điện
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

# 14. In cả giá trị và kiểu dữ liệu của hai kết quả
print("Với so_phut = 90")
print("dien_nang_kwh:", dien_nang_kwh, type(dien_nang_kwh))
print("chi_phi:", chi_phi, type(chi_phi))

# 16. Thay so_phut bằng 60 rồi chạy lại để so sánh
so_phut = 60
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("Với so_phut = 60")
print("dien_nang_kwh:", dien_nang_kwh, type(dien_nang_kwh))
print("chi_phi:", chi_phi, type(chi_phi))