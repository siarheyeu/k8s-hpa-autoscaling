# k8s-hpa-autoscaling

Demo project: Horizontal Pod Autoscaling (HPA) in Kubernetes with custom metrics, Prometheus, and Grafana.

## 🎯 What it does

- Deploys a Python FastAPI app to Kubernetes
- Configures HPA based on CPU and custom metrics (RPS)
- Exposes metrics via Prometheus
- Provides Grafana dashboard for visualization
- Includes load testing script

## 🛠️ Stack

- Kubernetes (HPA, Deployment, Service)
- Python (FastAPI, Prometheus client)
- Docker
- Prometheus + Grafana
- GitHub Actions (CI)

## 🚀 Quick start

```bash
# Deploy to Kubernetes
kubectl apply -f k8s/

# Run load test
python scripts/load-test.py

# Check HPA status
kubectl get hpa -n hpa-demo -w
```

## 📊 Architecture

Load Generator → Service → Pods (HPA scales) → Prometheus → Grafana

