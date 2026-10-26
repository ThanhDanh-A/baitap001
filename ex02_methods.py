"""
Bài tập 02: Methods & đóng gói 🔒
====================================
Mục tiêu: Instance methods, property, encapsulation
"""
import sys

# Đảm bảo in tiếng Việt chuẩn trên Windows console
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


# ==============================================================================
# TODO 1 & 2: Tạo class TaiKhoanNganHang có lịch sử giao dịch
# ==============================================================================
class TaiKhoanNganHang:
    def __init__(self, chu_tai_khoan: str, so_du: float = 0):
        self.chu_tai_khoan = chu_tai_khoan
        self.so_du = so_du
        self.lich_su = []
        if so_du > 0:
            self.lich_su.append(f"+{so_du:,.0f} VNĐ (Số dư ban đầu)")

    def gui_tien(self, so_tien: float) -> bool:
        if so_tien <= 0:
            print("❌ Số tiền gửi phải lớn hơn 0!")
            return False
        self.so_du += so_tien
        self.lich_su.append(f"+{so_tien:,.0f} VNĐ (Gửi tiền)")
        print(f"✅ Gửi {so_tien:,.0f} VNĐ thành công. Số dư hiện tại: {self.so_du:,.0f} VNĐ")
        return True

    def rut_tien(self, so_tien: float) -> bool:
        if so_tien <= 0:
            print("❌ Số tiền rút phải lớn hơn 0!")
            return False
        if so_tien > self.so_du:
            print(f"❌ Không đủ số dư! (Số dư hiện tại: {self.so_du:,.0f} VNĐ, cần rút: {so_tien:,.0f} VNĐ)")
            return False
        self.so_du -= so_tien
        self.lich_su.append(f"-{so_tien:,.0f} VNĐ (Rút tiền)")
        print(f"✅ Rút {so_tien:,.0f} VNĐ thành công. Số dư hiện tại: {self.so_du:,.0f} VNĐ")
        return True

    def xem_so_du(self) -> float:
        print(f"💰 Số dư của {self.chu_tai_khoan}: {self.so_du:,.0f} VNĐ")
        return self.so_du

    def xem_lich_su(self) -> None:
        print(f"📜 Lịch sử giao dịch ({self.chu_tai_khoan}):")
        if not self.lich_su:
            print("   (Chưa có giao dịch nào)")
        for idx, gd in enumerate(self.lich_su, 1):
            print(f"   {idx}. {gd}")

    def __str__(self) -> str:
        return f"TK {self.chu_tai_khoan}: {self.so_du:,.0f} VNĐ"


# ==============================================================================
# TODO 3: Tạo class SanPham
# ==============================================================================
class SanPham:
    def __init__(self, ten: str, gia: float, so_luong: int):
        self.ten = ten
        self.gia = gia
        self.so_luong = so_luong

    def ban(self, sl: int) -> bool:
        """Giảm số lượng sản phẩm nếu còn đủ hàng."""
        if sl <= 0:
            print("❌ Số lượng bán phải > 0!")
            return False
        if sl > self.so_luong:
            print(f"❌ Không đủ hàng! '{self.ten}' chỉ còn {self.so_luong} sản phẩm.")
            return False
        self.so_luong -= sl
        print(f"✅ Đã bán {sl} x '{self.ten}'. Tồn kho còn lại: {self.so_luong}")
        return True

    def nhap(self, sl: int) -> bool:
        """Tăng số lượng sản phẩm trong kho."""
        if sl <= 0:
            print("❌ Số lượng nhập phải > 0!")
            return False
        self.so_luong += sl
        print(f"✅ Đã nhập thêm {sl} x '{self.ten}'. Tồn kho hiện tại: {self.so_luong}")
        return True

    def tong_gia_tri(self) -> float:
        """Tổng giá trị tồn kho của sản phẩm = giá × số lượng."""
        return self.gia * self.so_luong

    def __str__(self) -> str:
        return f"'{self.ten}' | Giá: {self.gia:,.0f} VNĐ | Tồn kho: {self.so_luong}"


# ==============================================================================
# TODO 4 (Thử thách): Tạo class GioHang
# ==============================================================================
class GioHang:
    def __init__(self):
        # Lưu danh sách các mục: {"san_pham": SanPham, "so_luong": int}
        self.items = []

    def them(self, san_pham: SanPham, so_luong: int) -> bool:
        """Thêm sản phẩm vào giỏ hàng."""
        if so_luong <= 0:
            print("❌ Số lượng thêm vào giỏ phải > 0!")
            return False
        if so_luong > san_pham.so_luong:
            print(f"❌ '{san_pham.ten}' không đủ hàng trong kho (chỉ còn {san_pham.so_luong})!")
            return False

        # Kiểm tra xem sản phẩm đã có trong giỏ chưa
        for item in self.items:
            if item["san_pham"].ten.lower() == san_pham.ten.lower():
                item["so_luong"] += so_luong
                print(f"🛒 Đã tăng số lượng '{san_pham.ten}' trong giỏ lên {item['so_luong']}.")
                return True

        self.items.append({"san_pham": san_pham, "so_luong": so_luong})
        print(f"🛒 Đã thêm {so_luong} x '{san_pham.ten}' vào giỏ hàng.")
        return True

    def xoa(self, ten_san_pham: str) -> bool:
        """Xóa sản phẩm theo tên khỏi giỏ hàng."""
        for i, item in enumerate(self.items):
            if item["san_pham"].ten.lower() == ten_san_pham.lower():
                removed = self.items.pop(i)
                print(f"🗑️ Đã xóa '{removed['san_pham'].ten}' khỏi giỏ hàng.")
                return True
        print(f"❌ Không tìm thấy '{ten_san_pham}' trong giỏ hàng để xóa!")
        return False

    def tinh_tong(self) -> float:
        """Tính tổng số tiền của tất cả sản phẩm trong giỏ."""
        return sum(item["san_pham"].gia * item["so_luong"] for item in self.items)

    def hien_thi(self) -> None:
        """In danh sách sản phẩm trong giỏ hàng ra màn hình."""
        print("\n🛍️ --- CHI TIẾT GIỎ HÀNG ---")
        if not self.items:
            print("   (Giỏ hàng đang trống)")
            return
        for idx, item in enumerate(self.items, 1):
            sp = item["san_pham"]
            sl = item["so_luong"]
            thanh_tien = sp.gia * sl
            print(f"   {idx}. {sp.ten:<22} | SL: {sl:>2} | Đơn giá: {sp.gia:>10,.0f} | Thành tiền: {thanh_tien:>12,.0f} VNĐ")
        print("-" * 65)
        print(f"   👉 TỔNG TIỀN PHẢI THANH TOÁN: {self.tinh_tong():,.0f} VNĐ\n")


# ==============================================================================
# KIỂM TRA CHƯƠNG TRÌNH
# ==============================================================================
if __name__ == "__main__":
    print("=== KIỂM TRA TAIKHOANNGANHANG ===")
    tk = TaiKhoanNganHang("Nguyễn An", 1000000)
    tk.gui_tien(500000)
    tk.rut_tien(200000)
    tk.rut_tien(2000000)  # Thử rút quá số dư
    tk.xem_so_du()
    tk.xem_lich_su()
    print()

    print("=== KIỂM TRA SANPHAM & GIOHANG ===")
    sp1 = SanPham("Laptop Dell XPS", 25000000, 5)
    sp2 = SanPham("Chuột Logitech MX", 1800000, 20)
    sp3 = SanPham("Bàn phím cơ Keychron", 2200000, 15)

    print(sp1)
    print(f"Tổng giá trị kho {sp1.ten}: {sp1.tong_gia_tri():,.0f} VNĐ")
    sp1.ban(2)
    sp1.nhap(10)
    print()

    gio = GioHang()
    gio.them(sp1, 1)
    gio.them(sp2, 2)
    gio.them(sp3, 1)
    gio.hien_thi()

    gio.xoa("Chuột Logitech MX")
    gio.hien_thi()
