"""
Bài tập 03: Thiết kế class cho bài toán 🎨
=============================================
Mục tiêu: Tư duy OOP — thiết kế trước khi code
"""
import sys

# Đảm bảo in tiếng Việt chuẩn trên Windows console
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


# ==============================================================================
# TODO 1: Thiết kế class Sach
# ==============================================================================
class Sach:
    def __init__(self, tua_de: str, tac_gia: str, so_trang: int):
        self.tua_de = tua_de
        self.tac_gia = tac_gia
        self.so_trang = so_trang
        self.da_doc = 0

    def doc(self, so_trang: int) -> None:
        """Cập nhật số trang đã đọc thêm, không vượt quá tổng số trang."""
        if so_trang <= 0:
            print("Số trang đọc phải > 0!")
            return
        trang_cu = self.da_doc
        self.da_doc = min(self.so_trang, self.da_doc + so_trang)
        print(f"📖 Đã đọc thêm {self.da_doc - trang_cu} trang của cuốn '{self.tua_de}'.")

    def tien_do(self) -> float:
        """Tính phần trăm tiến độ đọc sách."""
        if self.so_trang == 0:
            return 0.0
        return (self.da_doc / self.so_trang) * 100

    def __str__(self) -> str:
        return f"\"{self.tua_de}\" ({self.tac_gia}) — Đã đọc: {self.da_doc}/{self.so_trang} trang ({self.tien_do():.1f}%)"


# ==============================================================================
# TODO 2: Thiết kế class DanhBa
# ==============================================================================
class LienHe:
    """Class đại diện cho một liên hệ trong danh bạ."""
    def __init__(self, ten: str, so_dien_thoai: str, email: str = ""):
        self.ten = ten
        self.so_dien_thoai = so_dien_thoai
        self.email = email

    def __str__(self) -> str:
        return f"{self.ten:<18} | SĐT: {self.so_dien_thoai:<12} | Email: {self.email}"


class DanhBa:
    def __init__(self):
        self.danh_sach: list[LienHe] = []

    def them(self, ten: str, sdt: str, email: str = "") -> None:
        """Thêm liên hệ mới."""
        lien_he = LienHe(ten, sdt, email)
        self.danh_sach.append(lien_he)
        print(f"✅ Đã thêm liên hệ: {ten} ({sdt})")

    def tim_theo_ten(self, tu_khoa: str) -> list[LienHe]:
        """Tìm kiếm liên hệ chứa từ khóa trong tên (không phân biệt hoa thường)."""
        ket_qua = [lh for lh in self.danh_sach if tu_khoa.lower() in lh.ten.lower()]
        return ket_qua

    def xoa(self, ten: str) -> bool:
        """Xóa liên hệ theo tên chính xác."""
        for i, lh in enumerate(self.danh_sach):
            if lh.ten.lower() == ten.lower():
                self.danh_sach.pop(i)
                print(f"🗑️ Đã xóa liên hệ '{lh.ten}'.")
                return True
        print(f"❌ Không tìm thấy liên hệ mang tên '{ten}' để xóa.")
        return False

    def hien_thi(self) -> None:
        """Hiển thị tất cả danh bạ."""
        print("\n📒 === DANH BẠ ĐIỆN THOẠI ===")
        if not self.danh_sach:
            print("   (Danh bạ đang trống)")
            return
        for idx, lh in enumerate(self.danh_sach, 1):
            print(f"   {idx}. {lh}")
        print("-" * 55)


# ==============================================================================
# TODO 3 (Thử thách): Thiết kế class QuanLyCafe
# ==============================================================================
class MonAn:
    def __init__(self, ma_mon: str, ten: str, gia: float, danh_muc: str):
        self.ma_mon = ma_mon
        self.ten = ten
        self.gia = gia
        self.danh_muc = danh_muc


class DonHang:
    dem_don = 0

    def __init__(self):
        DonHang.dem_don += 1
        self.ma_don = f"DH{DonHang.dem_don:03d}"
        self.chi_tiet = []  # list of {"mon": MonAn, "so_luong": int}

    def them_mon(self, mon: MonAn, so_luong: int = 1) -> None:
        for item in self.chi_tiet:
            if item["mon"].ma_mon == mon.ma_mon:
                item["so_luong"] += so_luong
                return
        self.chi_tiet.append({"mon": mon, "so_luong": so_luong})

    def tinh_tong_tien(self) -> float:
        return sum(item["mon"].gia * item["so_luong"] for item in self.chi_tiet)


class QuanLyCafe:
    def __init__(self, ten_quan: str):
        self.ten_quan = ten_quan
        self.menu: dict[str, MonAn] = {}

    def them_mon(self, ma_mon: str, ten: str, gia: float, danh_muc: str) -> None:
        self.menu[ma_mon] = MonAn(ma_mon, ten, gia, danh_muc)

    def in_menu(self) -> None:
        print(f"\n☕ ====== MENU QUÁN {self.ten_quan.upper()} ======")
        print(f"{'Mã':<6} {'Tên món':<22} {'Danh mục':<12} {'Giá (VNĐ)':>10}")
        print("-" * 55)
        for mon in self.menu.values():
            print(f"{mon.ma_mon:<6} {mon.ten:<22} {mon.danh_muc:<12} {mon.gia:>10,.0f}")
        print("-" * 55)

    def in_hoa_don(self, don_hang: DonHang) -> None:
        print(f"\n🧾 ===== HÓA ĐƠN THANH TOÁN - {self.ten_quan.upper()} =====")
        print(f"Mã đơn hàng: {don_hang.ma_don}")
        print("-" * 55)
        print(f"{'Tên món':<24} {'SL':>4} {'Đơn giá':>12} {'Thành tiền':>12}")
        print("-" * 55)
        for item in don_hang.chi_tiet:
            mon = item["mon"]
            sl = item["so_luong"]
            thanh_tien = mon.gia * sl
            print(f"{mon.ten:<24} {sl:>4} {mon.gia:>12,.0f} {thanh_tien:>12,.0f}")
        print("-" * 55)
        print(f"{'TỔNG CỘNG:':<40} {don_hang.tinh_tong_tien():>12,.0f} VNĐ\n")


# ==============================================================================
# KIỂM TRA CHƯƠNG TRÌNH
# ==============================================================================
if __name__ == "__main__":
    print("=== 1. KIỂM TRA CLASS SACH ===")
    s1 = Sach("Think Python", "Allen Downey", 300)
    s2 = Sach("Clean Code", "Robert C. Martin", 464)

    s1.doc(75)
    s2.doc(150)
    s2.doc(50)

    print(s1)
    print(s2)
    print()

    print("=== 2. KIỂM TRA CLASS DANHBA ===")
    db = DanhBa()
    db.them("Nguyễn Văn An", "0901234567", "an@gmail.com")
    db.them("Trần Thị Bình", "0912345678", "binh@gmail.com")
    db.them("Lê Hoàng Châu", "0987654321", "chau@gmail.com")
    db.hien_thi()

    print("🔍 Tìm kiếm liên hệ có chữ 'Châu':")
    for kq in db.tim_theo_ten("Châu"):
        print(f"   -> {kq}")

    db.xoa("Trần Thị Bình")
    db.hien_thi()

    print("=== 3. KIỂM TRA CLASS QUANLYCAFE ===")
    cafe = QuanLyCafe("The Coffee House")
    cafe.them_mon("CF01", "Cà phê đen đá", 29000, "Cà phê")
    cafe.them_mon("CF02", "Cà phê sữa đá", 35000, "Cà phê")
    cafe.them_mon("TR01", "Trà đào cam sả", 49000, "Trà trái cây")
    cafe.them_mon("BK01", "Bánh Croissant", 32000, "Bánh ngọt")

    cafe.in_menu()

    # Khách đặt đơn hàng
    don = DonHang()
    don.them_mon(cafe.menu["CF02"], 2)  # 2 Cà phê sữa đá
    don.them_mon(cafe.menu["TR01"], 1)  # 1 Trà đào cam sả
    don.them_mon(cafe.menu["BK01"], 2)  # 2 Bánh Croissant

    cafe.in_hoa_don(don)
