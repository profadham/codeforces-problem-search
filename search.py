import requests
from bs4 import BeautifulSoup
import time

KEYWORDS = ["construct","permutation"]   # <<< CHANGE THIS
MATCH_ALL = True                      # False = OR, True = AND

KEYWORDS = [k.lower() for k in KEYWORDS]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

results = []

print("Fetching all problems from API...")
try:
    r = requests.get("https://codeforces.com/api/problemset.problems", headers=headers, timeout=30)
    if r.status_code != 200:
        print(f"API Error: {r.status_code}")
        exit(1)
    
    data = r.json()
    if data.get("status") != "OK":
        print(f"API returned error status: {data.get('status')}")
        exit(1)
    
    problems = data["result"]["problems"]
    print(f"Found {len(problems)} problems\n")
    
    for idx, problem in enumerate(problems):
        if idx % 100 == 0:
            print(f"Processing problem {idx}...")
        
        # Get problem name and tags
        name = problem.get("name", "").lower()
        tags = [t.lower() for t in problem.get("tags", [])]
        contest_id = problem.get("contestId")
        index = problem.get("index")
        
        # Build searchable text
        haystack = name + " " + " ".join(tags)
        
        # Check if keywords match
        if MATCH_ALL:
            ok = all(k in haystack for k in KEYWORDS)
        else:
            ok = any(k in haystack for k in KEYWORDS)
        
        if ok:
            link = f"https://codeforces.com/problemset/problem/{contest_id}/{index}"
            results.append((link, name, tags))
    
except Exception as e:
    print(f"Error: {e}")
    exit(1)

print("\n=== RESULTS ===\n")
for link, name, tags in results:
    print(f"{link}")
    print(f"  Name: {name}")
    print(f"  Tags: {', '.join(tags)}")
    print()

print(f"Total problems found: {len(results)}")
