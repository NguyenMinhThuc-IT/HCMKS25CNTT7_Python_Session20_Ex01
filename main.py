# Dữ liệu thống kê gốc (Tên tuyển thủ, Kills, Deaths, Assists)
player_data_list = [
    ("Faker", "10", "2", "8"),       # Dữ liệu chuẩn
    ("ShowMaker", "15", "0", "10"),  # Trường hợp đặc biệt: Deaths = 0
    ("Chovy", "12", "ba", "5")       # Trường hợp lỗi: Dữ liệu chứa chữ
]

def calculate_kda(kills, deaths, assists):
    """Tính toán chỉ số KDA dựa trên các thông số trận đấu.
    
    Args:
        kills (int): Số mạng hạ gục.
        deaths (int): Số lần bị hạ gục.
        assists (int): Số mạng hỗ trợ.
        
    Returns:
        float: Giá trị KDA tính toán được.
        
    Raises:
        ZeroDivisionError: Nếu số lần bị hạ gục bằng 0.
    """
    if deaths == 0:
        raise ZeroDivisionError("Deaths bằng 0 dẫn đến trận đấu Perfect Game.")
    
    return (kills + assists) / deaths

def process_tournament_kda(player_records):
    """Duyệt danh sách thống tuyển thủ, bẫy ngoại lệ và in bảng xếp hạng KDA."""
    print("--- BẢNG XẾP HẠNG KDA ---")
    
    for player_stat in player_records:
        player_name = player_stat[0]
        
        try:
            # Ép kiểu dữ liệu chuỗi sang số nguyên
            kills = int(player_stat[1])
            deaths = int(player_stat[2])
            assists = int(player_stat[3])
            
            # Gọi hàm tính toán chỉ số KDA
            kda_score = calculate_kda(kills, deaths, assists)
            print(f"Tuyển thủ {player_name} có chỉ số KDA là: {kda_score:.1f}")
            
        except ZeroDivisionError:
            # Xử lý trường hợp tuyển thủ không chết mạng nào
            print(f"Tuyển thủ {player_name}: KDA Hoàn hảo (Perfect Game)!")
            
        except ValueError:
            # Xử lý trường hợp dữ liệu đầu vào không phải là số hợp lệ
            print(f"Tuyển thủ {player_name}: Lỗi dữ liệu không hợp lệ!")
        
    print("--- HOÀN TẤT ---")

if __name__ == "__main__":
    # Kích hoạt hệ thống xử lý dữ liệu giải đấu
    process_tournament_kda(player_data_list)