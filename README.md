# DL Systems Design

A full-stack, production-grade deep learning system covering training, inference, monitoring, CI/CD, and deployment on AWS with support for HuggingFace models, batch and streaming inference, and modern MLOps practices.

---

## 📁 Project Structure
```
dl-systems-design/
├── configs/                       # Hydra configs
├── data/                          # Raw/batch input data
├── docker/                        # Dockerfile, ECS JSON, AWS deploy script
├── inference/                    
│   ├── server.py                  # FastAPI REST server
│   ├── batch_inference.py         # Batch inference logic
│   └── streaming_consumer.py      # Placeholder for Kafka/SQS
├── logs/                          # Server logs
├── metrics/                       # (Future) evaluation/monitoring scripts
├── models/                        # Model checkpoints
├── notebooks/                     # Prototyping/EDA
├── scripts/                       # CLI automation helpers (optional)
├── tests/                         # Unit tests
├── training/
│   ├── model.py                   # PyTorch Lightning model
│   ├── hf_model.py                # HuggingFace-based model
│   └── train.py                   # Training loop
├── deployment/
│   ├── ab_testing.md              # Strategy notes for rollout
│   └── terraform/                 # ECR, ECS, infra-as-code
├── .github/workflows/             # GitHub Actions pipeline
├── requirements.txt               # Python deps
├── .gitignore
├── .env
└── README.md
```

---

## ✅ Features Overview

| Module               | Status        | Description |
|---------------------|---------------|-------------|
| Training            | ✅ Complete   | PyTorch Lightning model with WandB, seed, early stopping |
| Inference (REST)    | ✅ Complete   | FastAPI REST with logging, versioned endpoint |
| Batch Inference     | ✅ Complete   | CLI-based inference using batch JSON files |
| Streaming Input     | ⚠️ Scaffold   | Kafka/SQS consumer stub in place |
| HuggingFace Support | ⚠️ Partial    | Loads HF model; tokenizer and trainer needed |
| A/B Testing         | ✅ Documented | Canary + versioned endpoints + traffic splitting |
| Blue/Green Deploy   | ✅ Strategy   | ECS dual-service config ready |
| Docker + CI/CD      | ✅ Complete   | GitHub Actions for lint/test/Docker |
| AWS Deployment      | ✅ Scripted   | ECS + ECR push scripts + Terraform init |

---

## 🧠 Training
```bash
python training/train.py
```
- Uses PyTorch Lightning
- Configurable with Hydra (`configs/config.yaml`)
- Logs to WandB (optional)
- Checkpoints to `models/`

---

## 🌐 Inference
### FastAPI
```bash
uvicorn inference.server:app --reload
```
- Endpoint: `POST /v1/predict`
- Input: `{ "input": [[...]] }`
- Returns predicted class

### Batch Inference
```bash
python inference/batch_inference.py
```
- Reads `data/batch_inputs.json`
- Writes `data/batch_outputs.json`

---

## 📦 Containerization (Docker)
```bash
docker build -t dl-system .
docker run -p 8000:8000 dl-system
```
- Uses `docker/Dockerfile`
- Uvicorn server starts on launch

---

## ⚙️ CI/CD (GitHub Actions)
Auto-run on `main` branch:
- Lint (`flake8`)
- Tests (`pytest`)
- Docker build

File: `.github/workflows/main.yml`

---

## ☁️ AWS Deployment

### ECR Push
```bash
bash docker/aws_start.sh
```

### ECS Task Registration
```bash
aws ecs register-task-definition --cli-input-json file://docker/ecs_task_definition.json
```

### Terraform Infra Setup
```bash
cd deployment/terraform
terraform init
terraform apply
```

---

## 🚦 Canary / A/B / Blue-Green

- Run both `v1` and `v2` services in ECS
- Use ALB weighted target groups
- Versioned endpoint routing (`/v1/predict`, `/v2/predict`)

Details in `deployment/ab_testing.md`

---

## ✅ Ready for Extension
- [ ] MLflow model tracking
- [ ] Prometheus & Grafana monitoring
- [ ] Streaming Kafka/SQS handler
- [ ] SageMaker integration
- [ ] HuggingFace full NLP pipeline (tokenizer + dataset)

---

## 📄 License
MIT License