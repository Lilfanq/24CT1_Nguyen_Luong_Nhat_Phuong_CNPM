import torch

def run_inference():
    x = torch.tensor([1.0, 2.0, 3.0])
    result = torch.sum(x).item()
    return f"Kết quả tính toán từ PyTorch Model: {result}"