"""
Bài tập Tuần 13: Xây dựng API Client gọi Public API (Cơ quan Vũ trụ NASA)
========================================================================
Mục tiêu theo SYLLABUS Tuần 13:
1. HTTP GET request tới public endpoint (không cần secret key).
2. Kiểm tra HTTP Status Code (200 OK).
3. Xử lý và phân tích cú pháp JSON response.
4. Bắt lỗi mạng (Network error) và xử lý Timeout an toàn.
5. Validate (kiểm tra tính hợp lệ) của dữ liệu nhận về.
6. Hỗ trợ tham số dòng lệnh CLI (sys.argv hoặc argparse).
7. Đóng gói hướng đối tượng (OOP) theo chuẩn tuần 13.
"""

import argparse
import json
import sys
import urllib.error
import urllib.request
from typing import Any, Dict, List, Optional

# Đảm bảo hiển thị tiếng Việt và emoji đẹp mắt trên console Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")


class NasaItem:
    """Class đại diện cho một tư liệu vũ trụ nhận từ NASA."""

    def __init__(self, title: str, date: str, description: str, nasa_id: str, preview_url: Optional[str] = None):
        self.title = title
        self.date = date
        self.description = description
        self.nasa_id = nasa_id
        self.preview_url = preview_url

    def __str__(self) -> str:
        tom_tat = (self.description[:120] + "...") if len(self.description) > 120 else self.description
        return (
            f"🚀 [{self.date}] {self.title}\n"
            f"   Mã tư liệu: {self.nasa_id}\n"
            f"   Nội dung  : {tom_tat}\n"
            f"   Hình ảnh  : {self.preview_url or 'Không có sẵn'}"
        )


class NasaApiClient:
    """Class API Client giao tiếp với Cơ quan Hàng không và Vũ trụ NASA."""

    NASA_IMAGE_API = "https://images-api.nasa.gov/search"
    ISS_LOCATION_API = "http://api.open-notify.org/iss-now.json"

    def __init__(self, timeout: int = 10):
        self.timeout = timeout
        self.headers = {
            "User-Agent": "PythonJourney-Week13-Client/1.0",
            "Accept": "application/json",
        }

    def fetch_data(self, url: str) -> Optional[Dict[str, Any]]:
        """
        Thực hiện HTTP GET request với xử lý lỗi mạng, timeout và status code.
        """
        req = urllib.request.Request(url, headers=self.headers)
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as response:
                # 1. Kiểm tra Status Code
                status_code = response.getcode()
                if status_code != 200:
                    print(f"⚠️ API phản hồi mã lỗi: {status_code}")
                    return None

                # 2. Đọc và parse JSON
                raw_data = response.read().decode("utf-8")
                return json.loads(raw_data)

        except urllib.error.HTTPError as e:
            print(f"❌ Lỗi HTTP từ máy chủ: Mã {e.code} - {e.reason}")
            return None
        except urllib.error.URLError as e:
            print(f"❌ Lỗi kết nối mạng: {e.reason}")
            return None
        except TimeoutError:
            print(f"❌ Yêu cầu vượt quá thời gian chờ ({self.timeout} giây)!")
            return None
        except json.JSONDecodeError:
            print("❌ Dữ liệu nhận về không đúng định dạng JSON!")
            return None

    def tim_kiem_tu_lieu_nasa(self, tu_khoa: str = "mars", so_luong: int = 3) -> List[NasaItem]:
        """
        Tìm kiếm hình ảnh / tư liệu từ thư viện mở của NASA (không cần API key).
        """
        url = f"{self.NASA_IMAGE_API}?q={urllib.parse.quote(tu_khoa)}&media_type=image"
        print(f"📡 Đang gửi HTTP GET tới NASA API: {url}...")
        
        data = self.fetch_data(url)
        if not data:
            return []

        # Validate cấu trúc dữ liệu JSON từ NASA
        items = data.get("collection", {}).get("items", [])
        if not items:
            print(f"ℹ️ Không tìm thấy tư liệu nào với từ khóa '{tu_khoa}'.")
            return []

        ket_qua = []
        for item in items[:so_luong]:
            data_list = item.get("data", [])
            if not data_list:
                continue

            info = data_list[0]
            title = info.get("title", "Không có tiêu đề")
            date = info.get("date_created", "Không rõ")[:10]
            desc = info.get("description", "Không có mô tả")
            nasa_id = info.get("nasa_id", "N/A")

            # Lấy URL hình ảnh thu nhỏ
            links = item.get("links", [])
            preview_url = links[0].get("href") if links else None

            ket_qua.append(NasaItem(title, date, desc, nasa_id, preview_url))

        return ket_qua

    def lay_toa_do_tram_iss(self) -> Optional[Dict[str, Any]]:
        """
        Lấy vị trí thời gian thực của Trạm Vũ Trụ Quốc Tế (ISS).
        """
        print(f"📡 Đang lấy tọa độ trực tiếp của Trạm Vũ Trụ ISS...")
        data = self.fetch_data(self.ISS_LOCATION_API)
        if not data or data.get("message") != "success":
            return None

        pos = data.get("iss_position", {})
        return {
            "latitude": pos.get("latitude"),
            "longitude": pos.get("longitude"),
            "timestamp": data.get("timestamp"),
        }


def main():
    parser = argparse.ArgumentParser(
        description="Ứng dụng CLI gọi API Cơ quan Hàng không & Vũ trụ NASA (Tuần 13)"
    )
    parser.add_argument(
        "-q", "--query", 
        type=str, 
        default="mars rover",
        help="Từ khóa tìm kiếm vũ trụ (ví dụ: 'apollo 11', 'moon', 'mars rover', 'jupiter', 'webb')"
    )
    parser.add_argument(
        "-n", "--num", 
        type=int, 
        default=3, 
        help="Số lượng kết quả cần lấy (mặc định: 3)"
    )
    parser.add_argument(
        "--iss", 
        action="store_true", 
        help="Lấy vị trí thời gian thực của Trạm Vũ Trụ ISS"
    )

    args = parser.parse_args()
    client = NasaApiClient(timeout=10)

    print("=" * 72)
    print(" 🌌 CHƯƠNG TRÌNH KHÁM PHÁ DỮ LIỆU VŨ TRỤ NASA - TUẦN 13 API/HTTP 🌌")
    print("=" * 72)

    # 1. Nếu có tùy chọn --iss hoặc chạy mặc định: hiển thị tọa độ ISS
    if args.iss:
        iss_pos = client.lay_toa_do_tram_iss()
        if iss_pos:
            print("\n🛸 [VỊ TRÍ TRẠM VŨ TRỤ QUỐC TẾ ISS THỜI GIAN THỰC]:")
            print(f"   • Vĩ độ (Latitude)  : {iss_pos['latitude']}°")
            print(f"   • Kinh độ (Longitude): {iss_pos['longitude']}°")
            print(f"   • Timestamp          : {iss_pos['timestamp']}")
            print("   👉 Trạm ISS đang bay trên quỹ đạo Trái Đất với tốc độ ~27,600 km/h!\n")
        return

    # 2. Tìm kiếm tư liệu vũ trụ NASA
    danh_sach = client.tim_kiem_tu_lieu_nasa(tu_khoa=args.query, so_luong=args.num)

    print(f"\n🔍 KẾT QUẢ TÌM KIẾM CHO TỪ KHÓA: '{args.query.upper()}' ({len(danh_sach)} kết quả)")
    print("-" * 72)
    for i, item in enumerate(danh_sach, 1):
        print(f"#{i}. {item}")
        print("-" * 72)

    # Lấy kèm vị trí thời gian thực của trạm ISS
    iss_pos = client.lay_toa_do_tram_iss()
    if iss_pos:
        print("\n🛸 [TIỆN ÍCH]: TỌA ĐỘ TRỰC TIẾP TRẠM VŨ TRỤ ISS:")
        print(f"   Vĩ độ: {iss_pos['latitude']}° | Kinh độ: {iss_pos['longitude']}°")
    
    print("=" * 72)
    print("✅ Hoàn thành truy vấn dữ liệu từ API NASA thành công!")
    print("=" * 72)


if __name__ == "__main__":
    main()
