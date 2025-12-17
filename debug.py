import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://codeforces.com/",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}

# Use a session to maintain cookies
session = requests.Session()
session.headers.update(headers)

# Get first page
print("Fetching first page...")
r = session.get("https://codeforces.com/problemset/page/1", timeout=10)
print(f"Status: {r.status_code}")

soup = BeautifulSoup(r.text, "html.parser")

# Check for table
table = soup.find("table", class_="problems")
print(f"Table found: {table is not None}")

if table:
    rows = table.find_all("tr")[1:]
    print(f"Rows found: {len(rows)}")
    
    if rows:
        first_row = rows[0]
        name_cell = first_row.find("td", class_="name")
        if name_cell:
            a_tag = name_cell.find("a")
            if a_tag:
                link = "https://codeforces.com" + a_tag["href"]
                print(f"\nTesting with: {link}")
                
                # Fetch problem page
                print("Fetching problem page...")
                problem_r = session.get(link, timeout=10)
                print(f"Problem page status: {problem_r.status_code}")
                
                problem_soup = BeautifulSoup(problem_r.text, "html.parser")
                
                # Find all divs and look for statement
                all_divs = problem_soup.find_all("div")
                print(f"Total divs: {len(all_divs)}")
                
                # Print all unique classes
                classes_set = set()
                for div in all_divs:
                    classes = div.get("class", [])
                    if classes:
                        classes_set.add(tuple(classes))
                
                print("\nAll unique div classes containing 'problem' or 'statement':")
                for classes in sorted(classes_set):
                    class_str = " ".join(classes)
                    if "problem" in class_str.lower() or "statement" in class_str.lower():
                        print(f"  {class_str}")
