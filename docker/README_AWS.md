# Deploying to AWS (ECS Fargate + ECR)

### Prerequisites
- AWS CLI configured (`aws configure`)
- Docker installed
- Permissions to push to ECR and deploy to ECS

---

## 1. Create an ECR Repo
```bash
aws ecr create-repository --repository-name dl-system --region us-west-2
```

## 2. Build and Push Docker Image
```bash
cd docker
bash aws_start.sh
```

## 3. Register ECS Task Definition
Replace `<REPLACE_WITH_ECR_IMAGE_URI>` in `ecs_task_definition.json` with your actual ECR image URI.

```bash
aws ecs register-task-definition --cli-input-json file://ecs_task_definition.json
```

## 4. Run Task on ECS
```bash
aws ecs run-task \
  --cluster default \
  --launch-type FARGATE \
  --network-configuration 'awsvpcConfiguration={subnets=[subnet-abc123],securityGroups=[sg-xyz456],assignPublicIp="ENABLED"}' \
  --task-definition dl-system-task
```

---

Monitor with:
```bash
aws logs describe-log-groups
```

---

For full-scale deployment, use Terraform or AWS CDK.
