import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

# Try API endpoint
print("Trying API endpoint...")
r = requests.get("https://codeforces.com/api/problemset.problems", headers=headers, timeout=10)
print(f"API Status: {r.status_code}")
print(f"Response length: {len(r.text)}")

if r.status_code == 200:
    data = r.json()
    if "result" in data and "problems" in data["result"]:
        problems = data["result"]["problems"]
        print(f"Found {len(problems)} problems")
        print("\nFirst problem:")
        print(problems[0])
