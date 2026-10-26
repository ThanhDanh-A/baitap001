"""
Bài tập 03: Đa hình (Polymorphism) 🎭
========================================
Mục tiêu: Hiểu và áp dụng đa hình
"""

import math


# ==============================================================================
# TODO 1: Đa hình qua method chung
# ==============================================================================
class HinhTron:
    def __init__(self, ban_kinh):
        if ban_kinh <= 0:
            raise ValueError("Bán kính phải lớn hơn 0.")
        self.ban_kinh = ban_kinh

    def tinh_dien_tich(self):
        return math.pi * self.ban_kinh ** 2


class HinhChuNhat:
    def __init__(self, dai, rong):
        if dai <= 0 or rong <= 0:
            raise ValueError("Các cạnh phải lớn hơn 0.")
        self.dai = dai
        self.rong = rong

    def tinh_dien_tich(self):
        return self.dai * self.rong


class HinhTamGiac:
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Các cạnh phải lớn hơn 0.")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Ba cạnh không tạo thành tam giác.")
        self.a = a
        self.b = b
        self.c = c

    def tinh_dien_tich(self):
        # Công thức Heron
        nua_chu_vi = (self.a + self.b + self.c) / 2
        return math.sqrt(
            nua_chu_vi
            * (nua_chu_vi - self.a)
            * (nua_chu_vi - self.b)
            * (nua_chu_vi - self.c)
        )


# ==============================================================================
# TODO 2: Đa hình với "hợp đồng" thanh toán
# ==============================================================================
class ThanhToan:
    def phuong_thuc(self):
        raise NotImplementedError("Lớp con cần định nghĩa phuong_thuc().")

    def xu_ly(self, so_tien):
        raise NotImplementedError("Lớp con cần định nghĩa xu_ly(so_tien).")


class TienMat(ThanhToan):
    def phuong_thuc(self):
        return "Tiền mặt"

    def xu_ly(self, so_tien):
        return f"Nhận tiền mặt: {so_tien:,.0f} đồng."


class TheNganHang(ThanhToan):
    def phuong_thuc(self):
        return "Thẻ ngân hàng"

    def xu_ly(self, so_tien):
        return f"Trừ thẻ ngân hàng: {so_tien:,.0f} đồng."


class ViDienTu(ThanhToan):
    def phuong_thuc(self):
        return "Ví điện tử"

    def xu_ly(self, so_tien):
        return f"Chuyển qua ví điện tử: {so_tien:,.0f} đồng."


def thanh_toan(don_hang, phuong_thuc):
    """Xử lý thanh toán bằng bất kỳ đối tượng nào có phương thức xu_ly()."""
    if don_hang < 0:
        raise ValueError("Số tiền đơn hàng không được âm.")
    print(f"Đơn hàng: {don_hang:,.0f} đồng")
    print(f"Phương thức: {phuong_thuc.phuong_thuc()}")
    print(phuong_thuc.xu_ly(don_hang))


# ==============================================================================
# TODO 3: Duck typing — object nào có speak() đều dùng được
# ==============================================================================
class Cho:
    def speak(self):
        return "Gâu gâu!"


class Meo:
    def speak(self):
        return "Meo meo!"


class Robot:
    """Không kế thừa Cho hoặc Meo nhưng vẫn có speak()."""

    def speak(self):
        return "Xin chào, tôi là robot!"


def goi_speak(obj):
    """Duck typing: chỉ cần object có speak() là có thể gọi."""
    if not callable(getattr(obj, "speak", None)):
        raise TypeError("Đối tượng phải có phương thức speak().")
    print(obj.speak())


# ==============================================================================
# TODO 4 (Thử thách): Hệ thống nhân viên và đa hình tính lương
# ==============================================================================
class NhanVien:
    def __init__(self, ten):
        self.ten = ten

    def tinh_luong(self):
        raise NotImplementedError("Lớp con cần định nghĩa tinh_luong().")


class FullTime(NhanVien):
    def __init__(self, ten, luong_thang):
        super().__init__(ten)
        if luong_thang < 0:
            raise ValueError("Lương không được âm.")
        self.luong_thang = luong_thang

    def tinh_luong(self):
        return self.luong_thang


class PartTime(NhanVien):
    def __init__(self, ten, so_gio, luong_moi_gio):
        super().__init__(ten)
        if so_gio < 0 or luong_moi_gio < 0:
            raise ValueError("Số giờ và lương mỗi giờ không được âm.")
        self.so_gio = so_gio
        self.luong_moi_gio = luong_moi_gio

    def tinh_luong(self):
        return self.so_gio * self.luong_moi_gio


class Intern(NhanVien):
    def __init__(self, ten, tro_cap):
        super().__init__(ten)
        if tro_cap < 0:
            raise ValueError("Trợ cấp không được âm.")
        self.tro_cap = tro_cap

    def tinh_luong(self):
        return self.tro_cap


def tong_luong(danh_sach_nhan_vien):
    """Cộng lương của các loại nhân viên thông qua cùng method tinh_luong()."""
    return sum(nhan_vien.tinh_luong() for nhan_vien in danh_sach_nhan_vien)


def main():
    print("=== TODO 1: Đa hình qua method chung ===")
    cac_hinh = [HinhTron(5), HinhChuNhat(4, 6), HinhTamGiac(3, 4, 5)]
    for hinh in cac_hinh:
        print(f"{type(hinh).__name__}: diện tích = {hinh.tinh_dien_tich():.2f}")

    print("\n=== TODO 2: Đa hình thanh toán ===")
    cac_phuong_thuc = [TienMat(), TheNganHang(), ViDienTu()]
    for phuong_thuc in cac_phuong_thuc:
        thanh_toan(250_000, phuong_thuc)
        print()

    print("=== TODO 3: Duck typing ===")
    for doi_tuong in [Cho(), Meo(), Robot()]:
        goi_speak(doi_tuong)

    print("\n=== TODO 4: Đa hình tính lương nhân viên ===")
    danh_sach = [
        FullTime("An", 12_000_000),
        PartTime("Bình", 80, 30_000),
        Intern("Châu", 3_000_000),
    ]
    for nhan_vien in danh_sach:
        print(f"{nhan_vien.ten}: {nhan_vien.tinh_luong():,.0f} đồng")
    print(f"Tổng lương: {tong_luong(danh_sach):,.0f} đồng")


if __name__ == "__main__":
    main()
