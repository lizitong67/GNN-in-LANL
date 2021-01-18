"""
Autoencoders for Anomaly detection
Author:	Alston
Date: 2021.1.18
"""
import torch.nn as nn
import torch.nn.functional as F


class Autoencoder(nn.Module):
    def __init__(self):
        super(Autoencoder, self).__init__()

        # encoder
        self.enc1 = nn.Linear(in_features=20, out_features=16)
        self.enc2 = nn.Linear(in_features=16, out_features=8)
        self.enc3 = nn.Linear(in_features=8, out_features=4)
        self.enc4 = nn.Linear(in_features=4, out_features=2)

        # decoder
        self.dec1 = nn.Linear(in_features=2, out_features=4)
        self.dec2 = nn.Linear(in_features=4, out_features=8)
        self.dec3 = nn.Linear(in_features=8, out_features=16)
        self.dec4 = nn.Linear(in_features=16, out_features=20)


    def forward(self, x):
        x = F.relu(self.enc1(x))
        x = F.relu(self.enc2(x))
        x = F.relu(self.enc3(x))
        x = F.relu(self.enc4(x))

        x = F.relu(self.dec1(x))
        x = F.relu(self.dec2(x))
        x = F.relu(self.dec3(x))
        x = F.relu(self.dec4(x))

        return x