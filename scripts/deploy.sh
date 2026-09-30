#!/bin/bash
set -e

echo "🚀 Deploying HPA demo app..."

# Build and push image
docker build -t ghcr.io/your-username/k8s-hpa-autoscaling:latest app/
docker push ghcr.io/your-username/k8s-hpa-autoscaling:latest

# Apply Kubernetes manifests
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/hpa.yaml

echo "✅ Deployed! Check status:"
kubectl get pods -n hpa-demo
kubectl get hpa -n hpa-demo
