import torch
import torch.nn as nn
import pytorch_lightning as pl

class LitModel(pl.LightningModule):
    def __init__(self, input_dim=784, output_dim=10):
        super().__init__()
        self.layer = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ReLU(),
            nn.Linear(128, output_dim)
        )
        self.loss_fn = nn.CrossEntropyLoss()

    def forward(self, x):
        return self.layer(x)

    def training_step(self, batch, batch_idx):
        x, y = batch
        logits = self(x)
        loss = self.loss_fn(logits, y)
        self.log("train_loss", loss)
        return loss

    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(), lr=1e-3)
