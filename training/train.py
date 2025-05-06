import pytorch_lightning as pl
from pytorch_lightning.loggers import WandbLogger
from training.model import LitModel
from torch.utils.data import DataLoader, random_split
from torchvision.datasets import MNIST
from torchvision import transforms

pl.seed_everything(42)

def train():
    dataset = MNIST("./data", download=True, transform=transforms.ToTensor())
    train_set, val_set = random_split(dataset, [55000, 5000])

    train_loader = DataLoader(train_set, batch_size=64)
    val_loader = DataLoader(val_set, batch_size=64)

    model = LitModel()
    wandb_logger = WandbLogger(project="dl-systems-design")
    trainer = pl.Trainer(max_epochs=10, logger=wandb_logger)
    trainer.fit(model, train_loader, val_loader)

if __name__ == "__main__":
    train()
