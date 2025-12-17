from flask import Flask, render_template, request, jsonify
import requests
import threading

app = Flask(__name__)

# Global variables to store state
search_results = []
is_searching = False
search_cache = None
cache_time = 0

def fetch_problems():
    """Fetch all problems from Codeforces API"""
    global search_cache, cache_time
    import time
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    print("Fetching problems from API...")
    r = requests.get("https://codeforces.com/api/problemset.problems", headers=headers, timeout=30)
    
    if r.status_code == 200:
        data = r.json()
        if data.get("status") == "OK":
            search_cache = data["result"]["problems"]
            cache_time = time.time()
            return search_cache
    
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/search', methods=['POST'])
def search():
    """Search for problems based on keywords"""
    global is_searching, search_cache
    
    if is_searching:
        return jsonify({'status': 'searching', 'message': 'Search already in progress'})
    
    data = request.json
    keywords = data.get('keywords', '').strip().split()
    match_all = data.get('match_all', False)
    
    if not keywords:
        return jsonify({'status': 'error', 'message': 'Please enter at least one keyword'})
    
    keywords = [k.lower() for k in keywords]
    
    # Fetch problems if not cached
    if search_cache is None:
        problems = fetch_problems()
        if problems is None:
            return jsonify({'status': 'error', 'message': 'Failed to fetch problems from Codeforces API'})
    else:
        problems = search_cache
    
    results = []
    
    for problem in problems:
        name = problem.get("name", "").lower()
        tags = [t.lower() for t in problem.get("tags", [])]
        contest_id = problem.get("contestId")
        index = problem.get("index")
        
        haystack = name + " " + " ".join(tags)
        
        if match_all:
            ok = all(k in haystack for k in keywords)
        else:
            ok = any(k in haystack for k in keywords)
        
        if ok:
            link = f"https://codeforces.com/problemset/problem/{contest_id}/{index}"
            results.append({
                'link': link,
                'name': problem.get("name", ""),
                'tags': tags,
                'contestId': contest_id,
                'index': index
            })
    
    return jsonify({
        'status': 'success',
        'count': len(results),
        'results': results
    })

@app.route('/api/cache-status', methods=['GET'])
def cache_status():
    """Check if problems are cached"""
    global search_cache, cache_time
    
    if search_cache is None:
        return jsonify({'cached': False, 'count': 0})
    else:
        return jsonify({'cached': True, 'count': len(search_cache)})

@app.route('/api/load-cache', methods=['POST'])
def load_cache():
    """Pre-load all problems into cache"""
    global is_searching, search_cache
    
    if is_searching:
        return jsonify({'status': 'error', 'message': 'Already loading'})
    
    if search_cache is not None:
        return jsonify({'status': 'success', 'message': 'Problems already cached', 'count': len(search_cache)})
    
    is_searching = True
    
    def load():
        global is_searching
        problems = fetch_problems()
        is_searching = False
        return problems is not None
    
    thread = threading.Thread(target=load)
    thread.start()
    
    return jsonify({'status': 'loading', 'message': 'Loading problems in background'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
