import requests
import time
import json

API_URL = "http://localhost:5000/summarize"
SAMPLE_TEXT = "Cohere provides API access to cutting-edge large language models. " * 50

TEST_CASES = [
    {"name": "Normal paragraph", "payload": {"text": SAMPLE_TEXT}},
    {"name": "Short sentence", "payload": {"text": "Test."}},
    {"name": "Empty string", "payload": {"text": ""}},
    {"name": "Large input", "payload": {"text": open('large_text.txt').read()}},
    {"name": "Malformed request", "payload": {"wrong_key": "data"}},
]

def run_tests():
    # Single request tests
    for test in TEST_CASES:
        try:
            start = time.perf_counter()
            response = requests.post(API_URL, json=test['payload'])
            latency = (time.perf_counter() - start) * 1000
            
            print(f"\n{test['name']}:")
            print(f"Status: {response.status_code}")
            print(f"Latency: {latency:.2f}ms")
            print("Response:", json.dumps(response.json(), indent=2)[:200] + "...")
            
        except Exception as e:
            print(f"{test['name']} FAILED: {str(e)}")
    
    # Load test
    print("\nStarting load test (20 sequential requests)...")
    start_time = time.time()
    for i in range(20):
        try:
            requests.post(API_URL, json={"text": f"Load test request #{i}. {SAMPLE_TEXT}"})
            print(f"Request {i+1}/20 completed")
        except Exception as e:
            print(f"Request failed: {str(e)}")
    print(f"Load test completed in {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    # Generate large text file for testing
    with open('large_text.txt', 'w') as f:
        f.write("Large text " * 10000)  # ~100K words
        
    run_tests()