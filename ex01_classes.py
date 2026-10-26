"""
Bài tập 01: Class đầu tiên 🏗️
================================
Mục tiêu: Định nghĩa class, __init__, tạo object
"""

# ==============================================================================
# TODO 1: Tạo class HocSinh với:
# - __init__(self, ten, tuoi, diem)
# - Tạo 3 object và in ra thông tin
# ==============================================================================
class HocSinh:
    # TODO 4 (Thử thách): Class variable
    # Thêm class variable dem = 0, tăng mỗi khi tạo HocSinh mới
    dem = 0

    def __init__(self, ten, tuoi, diem):
        self.ten = ten
        self.tuoi = tuoi
        self.diem = diem
        HocSinh.dem += 1

    # TODO 2: Thêm method tinh_xep_loai(self)
    # >= 9: "Xuất sắc", >= 8: "Giỏi", >= 6.5: "Khá", >= 5: "TB", < 5: "Yếu"
    # Gọi: hs.tinh_xep_loai()
    def tinh_xep_loai(self):
        if self.diem >= 9:
            return "Xuất sắc"
        elif self.diem >= 8:
            return "Giỏi"
        elif self.diem >= 6.5:
            return "Khá"
        elif self.diem >= 5:
            return "TB"
        return "Yếu"

    # TODO 3: Thêm __str__(self) trả về chuỗi đẹp
    # print(hs) → "Nguyễn An (20 tuổi) - Điểm: 8.5 - Giỏi"
    def __str__(self):
        return f"{self.ten} ({self.tuoi} tuổi) - Điểm: {self.diem} - {self.tinh_xep_loai()}"

    # TODO 4 (Thử thách): Class method so_luong() trả về tổng số học sinh
    @classmethod
    def so_luong(cls):
        return cls.dem


# ==============================================================================
# THỰC THI & KIỂM TRA TỪNG TODO
# ==============================================================================
print("--- TODO 1 & TODO 3: Tạo 3 object và in ra thông tin bằng print(hs) ---")
hs1 = HocSinh("Nguyễn An", 20, 8.5)
hs2 = HocSinh("Trần Bình", 21, 6.0)
hs3 = HocSinh("Lê Châu", 20, 9.5)

print(hs1)
print(hs2)
print(hs3)
print()

print("--- TODO 2: Gọi method hs.tinh_xep_loai() ---")
print(f"{hs1.ten}: {hs1.tinh_xep_loai()}")
print(f"{hs2.ten}: {hs2.tinh_xep_loai()}")
print(f"{hs3.ten}: {hs3.tinh_xep_loai()}")
print()

print("--- TODO 4: Kiểm tra tổng số học sinh từ class method ---")
print(f"Tổng số học sinh đã tạo: {HocSinh.so_luong()}")
