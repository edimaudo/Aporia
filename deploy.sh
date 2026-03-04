#!/bin/bash
# Socratic Shadow Deployment Script

PROJECT_ID=$(gcloud config get-value project)
SERVICE_NAME="aporia-backend"

echo "Deploying Aporia to Google Cloud..."

gcloud run deploy $SERVICE_NAME \
  --source . \
  --region us-central1 \
  --allow-unauthenticated \
  --timeout=3600 \
  --concurrency=50 \
  --no-cpu-throttling \
  --set-env-vars="GEMINI_API_KEY=your_key_here,PROJECT_ID=$PROJECT_ID"

echo "Deployment complete. Face your shadow."
