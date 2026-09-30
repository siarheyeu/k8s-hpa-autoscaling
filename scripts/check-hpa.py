#!/usr/bin/env python3
"""
Check HPA status in Kubernetes.
Requires: kubectl configured, kubernetes Python client.
"""

from kubernetes import client, config
import sys

NAMESPACE = "hpa-demo"
HPA_NAME = "hpa-demo-app"

def main():
    config.load_kube_config()
    autoscaling = client.AutoscalingV2Api()

    hpa = autoscaling.read_namespaced_horizontal_pod_autoscaler(
        name=HPA_NAME, namespace=NAMESPACE
    )

    print(f"📊 HPA: {hpa.metadata.name}")
    print(f"   Min replicas: {hpa.spec.min_replicas}")
    print(f"   Max replicas: {hpa.spec.max_replicas}")
    print(f"   Current replicas: {hpa.status.current_replicas}")
    print(f"   Desired replicas: {hpa.status.desired_replicas}")
    print(f"   Current metrics:")
    for m in hpa.status.current_metrics or []:
        print(f"     - {m.type}: {m.resource.current.average_utilization}%")

if __name__ == "__main__":
    main()
