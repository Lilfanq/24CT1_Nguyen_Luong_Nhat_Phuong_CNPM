import torch

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
MODEL_PATH = "weights/model.pth"
SERVER_NAME = "127.0.0.1"