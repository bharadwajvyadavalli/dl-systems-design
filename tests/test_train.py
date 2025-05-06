from training.model import LitModel
import torch

def test_model_output():
    model = LitModel()
    output = model.forward(torch.randn(1, 784))
    assert output.shape == (1, 10)
