from fastapi import FastAPI, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time
import random

app = FastAPI(title="HPA Demo App")

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "status"]
)

REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "HTTP request latency",
    ["endpoint"]
)

@app.get("/")
def root():
    REQUEST_COUNT.labels(method="GET", endpoint="/", status="200").inc()
    with REQUEST_LATENCY.labels(endpoint="/").time():
        # Simulate CPU load
        time.sleep(random.uniform(0.01, 0.05))
    return {"status": "ok", "message": "HPA Demo App"}

@app.get("/heavy")
def heavy():
    REQUEST_COUNT.labels(method="GET", endpoint="/heavy", status="200").inc()
    with REQUEST_LATENCY.labels(endpoint="/heavy").time():
        # Simulate heavy CPU work
        total = 0
        for i in range(10_000_000):
            total += i * i
    return {"status": "ok", "result": total}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.get("/health")
def health():
    return {"status": "healthy"}
