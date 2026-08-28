import os
import pandas as pd

def create_sample_data():
    # Tạo dữ liệu mẫu
    data = {
        "text": ["Chào mừng CNPM", "Học phần AI", "Yêu cầu nhận thức 1"],
        "label": [1, 1, 0]
    }
    df = pd.DataFrame(data)
    
    # Lưu vào thư mục data/raw
    os.makedirs("data/raw", exist_ok=True)
    df.to_csv("data/raw/sample_dataset.csv", index=False)
    print("Đã tạo dữ liệu mẫu tại: data/raw/sample_dataset.csv")

if __name__ == "__main__":
    create_sample_data()