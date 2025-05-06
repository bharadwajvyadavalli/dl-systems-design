from fastapi import FastAPI
from pydantic import BaseModel
import torch
from training.model import LitModel
from loguru import logger

app = FastAPI()
model = LitModel()
model.load_state_dict(torch.load("models/model.pt"))
model.eval()

logger.add("logs/server.log")

class Request(BaseModel):
    input: list

@app.post("/v1/predict")
def predict(req: Request):
    logger.info("Received request: {}", req.input)
    with torch.no_grad():
        x = torch.tensor(req.input).float()
        preds = model(x)
        return {"prediction": preds.argmax(dim=1).tolist()}
