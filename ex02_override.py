"""
Bài tập 02: Override & super() 🔄
===================================
Mục tiêu: Ghi đè phương thức, gọi class cha
"""


# ==============================================================================
# TODO 1 & TODO 2: Override __str__ và phương thức tính lương
# ==============================================================================
class NhanVien:
    def __init__(self, ten, luong):
        if luong < 0:
            raise ValueError("Lương không được âm.")
        self.ten = ten
        self.luong = luong

    def __str__(self):
        return f"Nhân viên: {self.ten} - Lương cơ bản: {self.luong:,.0f} đồng"

    def tinh_luong(self):
        """Nhân viên bình thường nhận 100% lương cơ bản."""
        return self.luong


class QuanLy(NhanVien):
    def __init__(self, ten, luong, phong_ban):
        super().__init__(ten, luong)
        self.phong_ban = phong_ban

    def __str__(self):
        return f"{super().__str__()} - Phòng ban: {self.phong_ban}"

    def tinh_luong(self):
        """Quản lý nhận thêm phụ cấp 20% lương cơ bản."""
        return self.luong * 1.2


class TapSu(NhanVien):
    def tinh_luong(self):
        """Thực tập sinh nhận 70% lương cơ bản."""
        return self.luong * 0.7


# ==============================================================================
# TODO 3: Dùng super().__init__() với Vehicle và ElectricCar
# ==============================================================================
class Vehicle:
    def __init__(self, name, speed):
        if speed < 0:
            raise ValueError("Tốc độ không được âm.")
        self.name = name
        self.speed = speed

    def __str__(self):
        return f"{self.name} - Tốc độ tối đa: {self.speed} km/h"


class ElectricCar(Vehicle):
    def __init__(self, name, speed, battery):
        super().__init__(name, speed)
        if battery < 0:
            raise ValueError("Dung lượng pin không được âm.")
        self.battery = battery

    def __str__(self):
        return f"{super().__str__()} - Pin: {self.battery} kWh"


# ==============================================================================
# TODO 4 (Thử thách): Template Method Pattern
# ==============================================================================
class Report:
    """generate() cố định thứ tự tạo báo cáo; lớp con tùy chỉnh từng phần."""

    def header(self):
        return "===== BÁO CÁO ====="

    def body(self):
        raise NotImplementedError("Lớp con cần định nghĩa body().")

    def footer(self):
        return "===== KẾT THÚC ====="

    def generate(self):
        return "\n".join([self.header(), self.body(), self.footer()])


class HTMLReport(Report):
    def header(self):
        return "<html><body><h1>Báo cáo</h1>"

    def body(self):
        return "<p>Đây là nội dung báo cáo HTML.</p>"

    def footer(self):
        return "</body></html>"


class TextReport(Report):
    def body(self):
        return "Đây là nội dung báo cáo văn bản thuần."


def main():
    print("=== TODO 1: Override __str__ ===")
    nhan_vien = NhanVien("An", 10_000_000)
    quan_ly = QuanLy("Bình", 20_000_000, "Kỹ thuật")
    print(nhan_vien)
    print(quan_ly)

    print("\n=== TODO 2: Override tính lương ===")
    tap_su = TapSu("Châu", 8_000_000)
    for nguoi in [nhan_vien, quan_ly, tap_su]:
        print(f"{nguoi.ten}: {nguoi.tinh_luong():,.0f} đồng")

    print("\n=== TODO 3: super().__init__() ===")
    xe_dien = ElectricCar("Xe điện", 160, 75)
    print(xe_dien)

    print("\n=== TODO 4: Template Method Pattern ===")
    print("-- Báo cáo HTML --")
    print(HTMLReport().generate())
    print("-- Báo cáo văn bản --")
    print(TextReport().generate())


if __name__ == "__main__":
    main()
