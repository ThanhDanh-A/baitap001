"""
Bài tập 01: Kế thừa cơ bản 🧬
================================
Mục tiêu: Tạo class con kế thừa class cha
"""

import math


# ==============================================================================
# PHẦN 1: Kế thừa cơ bản với DongVat, Cho và Meo
# ==============================================================================
class DongVat:
    """Class cha mô tả các đặc điểm chung của động vật."""

    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi

    def an(self):
        print(f"{self.ten} đang ăn.")

    def ngu(self):
        print(f"{self.ten} đang ngủ.")


class Cho(DongVat):
    """Chó kế thừa DongVat và có thêm giống chó."""

    def __init__(self, ten, tuoi, giong):
        super().__init__(ten, tuoi)
        self.giong = giong

    def sua(self):
        print(f"{self.ten} sủa: Gâu gâu!")


class Meo(DongVat):
    """Mèo kế thừa DongVat và có thêm màu lông."""

    def __init__(self, ten, tuoi, mau_long):
        super().__init__(ten, tuoi)
        self.mau_long = mau_long

    def keu(self):
        print(f"{self.ten} kêu: Meo meo!")


# ==============================================================================
# PHẦN 2: Kế thừa với các hình học
# ==============================================================================
class HinhHoc:
    """Class cha cho các hình học."""

    def tinh_dien_tich(self):
        raise NotImplementedError("Lớp con cần định nghĩa tinh_dien_tich().")

    def tinh_chu_vi(self):
        raise NotImplementedError("Lớp con cần định nghĩa tinh_chu_vi().")


class HinhTron(HinhHoc):
    def __init__(self, ban_kinh):
        if ban_kinh <= 0:
            raise ValueError("Bán kính phải lớn hơn 0.")
        self.ban_kinh = ban_kinh

    def tinh_dien_tich(self):
        return math.pi * self.ban_kinh ** 2

    def tinh_chu_vi(self):
        return 2 * math.pi * self.ban_kinh

    def __str__(self):
        return (
            f"Hình tròn (bán kính = {self.ban_kinh}): "
            f"diện tích = {self.tinh_dien_tich():.2f}, "
            f"chu vi = {self.tinh_chu_vi():.2f}"
        )


class HinhChuNhat(HinhHoc):
    def __init__(self, dai, rong):
        if dai <= 0 or rong <= 0:
            raise ValueError("Chiều dài và chiều rộng phải lớn hơn 0.")
        self.dai = dai
        self.rong = rong

    def tinh_dien_tich(self):
        return self.dai * self.rong

    def tinh_chu_vi(self):
        return 2 * (self.dai + self.rong)

    def __str__(self):
        return (
            f"Hình chữ nhật ({self.dai} x {self.rong}): "
            f"diện tích = {self.tinh_dien_tich():.2f}, "
            f"chu vi = {self.tinh_chu_vi():.2f}"
        )


# ==============================================================================
# PHẦN 3: Kiểm tra quan hệ kế thừa bằng isinstance() và issubclass()
# ==============================================================================
def kiem_tra_ke_thua(doi_tuong):
    """In kết quả kiểm tra đối tượng có thuộc class cha/con hay không."""
    print(f"isinstance(doi_tuong, DongVat): {isinstance(doi_tuong, DongVat)}")
    print(f"isinstance(doi_tuong, Cho): {isinstance(doi_tuong, Cho)}")
    print(f"issubclass(Cho, DongVat): {issubclass(Cho, DongVat)}")
    print(f"issubclass(Meo, DongVat): {issubclass(Meo, DongVat)}")
    print(f"issubclass(DongVat, Cho): {issubclass(DongVat, Cho)}")


# ==============================================================================
# PHẦN 4: Đa kế thừa với Flyer, Swimmer và Duck
# ==============================================================================
class Flyer:
    def fly(self):
        print("Vịt đang bay.")


class Swimmer:
    def swim(self):
        print("Vịt đang bơi.")


class Duck(Flyer, Swimmer):
    def __init__(self, ten):
        self.ten = ten


def main():
    print("=== PHẦN 1: Kế thừa cơ bản ===")
    cho = Cho("Milu", 3, "Poodle")
    meo = Meo("Miu", 2, "Trắng")

    cho.an()
    cho.ngu()
    cho.sua()
    print(f"Giống chó: {cho.giong}")
    meo.an()
    meo.ngu()
    meo.keu()
    print(f"Màu lông mèo: {meo.mau_long}")

    print("\n=== PHẦN 2: Hình học ===")
    cac_hinh = [HinhTron(5), HinhChuNhat(4, 6)]
    for hinh in cac_hinh:
        print(hinh)

    print("\n=== PHẦN 3: Kiểm tra kế thừa ===")
    kiem_tra_ke_thua(cho)

    print("\n=== PHẦN 4: Đa kế thừa ===")
    vit = Duck("Vịt Donald")
    print(f"Tên: {vit.ten}")
    vit.fly()
    vit.swim()


if __name__ == "__main__":
    main()
