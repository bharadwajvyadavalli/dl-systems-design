#!/bin/bash
# This script assumes you have configured AWS CLI and have Docker installed

# ECR repo name
REPO_NAME=dl-system
AWS_REGION=us-west-2

# Authenticate Docker to ECR
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $(aws sts get-caller-identity --query 'Account' --output text).dkr.ecr.$AWS_REGION.amazonaws.com

# Build and tag Docker image
docker build -t $REPO_NAME .
ACCOUNT_ID=$(aws sts get-caller-identity --query "Account" --output text)
ECR_URI=$ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$REPO_NAME

# Tag and push image to ECR
docker tag $REPO_NAME:latest $ECR_URI:latest
docker push $ECR_URI:latest

echo "Image pushed to ECR: $ECR_URI"
