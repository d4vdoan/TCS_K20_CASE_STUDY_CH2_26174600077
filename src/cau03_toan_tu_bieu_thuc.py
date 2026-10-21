tong_phut = 135
cong_suat_w = 250

# 9. Dùng // và % để tính số giờ trọn vẹn và số phút còn lại
so_gio = tong_phut // 60
so_phut_con_lai = tong_phut % 60
print("Số giờ:", so_gio)
print("Số phút còn lại:", so_phut_con_lai)

# 10. Biến su_dung_lau nhận True khi tong_phut > 60
su_dung_lau = tong_phut > 60
print("su_dung_lau:", su_dung_lau)

# 11. Biến du_lieu_hop_le nhận True khi cong_suat_w > 0 và tong_phut > 0
du_lieu_hop_le = cong_suat_w > 0 and tong_phut > 0
print("du_lieu_hop_le:", du_lieu_hop_le)

# 12. Hai biểu thức cần dự đoán trước khi chạy
bieu_thuc_1 = 100 + 20 * 3
bieu_thuc_2 = (100 + 20) * 3
print("100 + 20 * 3 =", bieu_thuc_1)
print("(100 + 20) * 3 =", bieu_thuc_2)