import torch
import torch.nn as nn

class SampleModel(nn.Module):
    def __init__(self):
        super(SampleModel, self).__init__()
        self.fc = nn.Linear(10, 1)

    def forward(self, x):
        return self.fc(x)