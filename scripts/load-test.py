#!/usr/bin/env python3
"""
Load test script for HPA demo app.
Sends requests to /heavy endpoint to trigger HPA scaling.
"""

import requests
import time
import sys
from concurrent.futures import ThreadPoolExecutor

URL = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8000"
DURATION = int(sys.argv[2]) if len(sys.argv) > 2 else 60
CONCURRENCY = int(sys.argv[3]) if len(sys.argv) > 3 else 10

def send_request():
    try:
        r = requests.get(f"{URL}/heavy", timeout=10)
        return r.status_code
    except Exception as e:
        return str(e)

def main():
    print(f"🚀 Load testing {URL} for {DURATION}s with {CONCURRENCY} workers")
    start = time.time()
    count = 0
    errors = 0

    with ThreadPoolExecutor(max_workers=CONCURRENCY) as executor:
        while time.time() - start < DURATION:
            futures = [executor.submit(send_request) for _ in range(CONCURRENCY)]
            for f in futures:
                result = f.result()
                count += 1
                if result != 200:
                    errors += 1

    elapsed = time.time() - start
    print(f"✅ Done: {count} requests in {elapsed:.1f}s")
    print(f"📊 RPS: {count / elapsed:.1f}")
    print(f"❌ Errors: {errors}")

if __name__ == "__main__":
    main()
