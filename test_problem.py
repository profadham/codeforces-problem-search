import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

# Try getting a specific problem
contest_id = 2176
problem_index = "F"

print(f"Trying to fetch problem {contest_id}{problem_index}...")

# Try direct problem page
url = f"https://codeforces.com/problemset/problem/{contest_id}/{problem_index}"
print(f"URL: {url}")

r = requests.get(url, headers=headers, timeout=10)
print(f"Status: {r.status_code}")

if r.status_code == 200:
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(r.text, "html.parser")
    
    # Look for statement
    statement_div = soup.find("div", class_="problem-statement")
    if statement_div:
        text = statement_div.get_text()
        print(f"Found statement! Length: {len(text)}")
        print(text[:500])
    else:
        print("No statement div found")
        
        # Let's see what divs we have
        all_divs = soup.find_all("div")
        print(f"\nTotal divs: {len(all_divs)}")
        
        # Look for any div with statement-like content
        for div in all_divs[:20]:
            classes = div.get("class", [])
            if classes:
                print(f"  Classes: {' '.join(classes)}, Text length: {len(div.get_text())}")
