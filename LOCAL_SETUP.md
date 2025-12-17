# Local Setup & Development Guide

This guide explains how to clone and run the Codeforces Problem Search application locally on your machine.

## Prerequisites

Before you start, make sure you have:

- **Python 3.8 or higher** - Download from [python.org](https://www.python.org/downloads/)
- **Git** (optional, for cloning) - Download from [git-scm.com](https://git-scm.com)
- **A command line/terminal** - PowerShell, CMD, Bash, etc.

### Verify Installation

Open terminal and check:

```bash
python --version    # Should show Python 3.8+
pip --version       # Should show pip version
git --version       # Optional, should show git version
```

## Step-by-Step Setup

### 1. Clone the Repository

Choose one method:

**Option A: Using Git (Recommended)**
```bash
git clone https://github.com/profadham/codeforces-problem-search.git
cd codeforces-problem-search
```

**Option B: Download ZIP**
1. Go to https://github.com/profadham/codeforces-problem-search
2. Click "Code" (green button) → "Download ZIP"
3. Extract the ZIP file
4. Open terminal in the extracted folder

### 2. Create Virtual Environment (Recommended)

A virtual environment keeps your project dependencies isolated.

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` at the start of your terminal line when activated.

### 3. Install Dependencies

With the virtual environment activated, run:

```bash
pip install -r requirements.txt
```

This installs:
- Flask (web framework)
- Requests (HTTP library)
- BeautifulSoup4 (HTML parsing)

### 4. Run the Application

```bash
python app.py
```

You should see output like:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### 5. Open in Browser

Click on `http://localhost:5000` or manually visit:
```
http://127.0.0.1:5000
```

## Using the Application

### Basic Search

1. **Type keywords** - Enter problem keywords (space-separated)
   - Example: `construct` or `dynamic programming`

2. **Choose matching mode**
   - Unchecked (default): Match problems with **ANY** keyword
   - Checked: Match problems with **ALL** keywords

3. **Search** - Click the Search button or press Enter

4. **Browse results** - Click any problem link to open on Codeforces

### First Search Tips

- **First search is slow** (~2-3 seconds) - it fetches from Codeforces API
- **Pre-load cache** - Click "Pre-load Cache" to load all 10,000+ problems
- **Subsequent searches** - Will be instant after cache is loaded!

### Example Searches

```
Query: "construct"
→ All construction algorithm problems

Query: "dp"
→ Dynamic programming problems

Query: "construct array" (with ALL mode)
→ Problems with both "construct" AND "array"

Query: "graph greedy tree"
→ Graph, greedy, or tree problems (ANY mode)
```

## Stopping the Application

1. Go to your terminal
2. Press **Ctrl+C**
3. Virtual environment is still active - that's fine
4. To deactivate: type `deactivate` and press Enter

## Restarting the Application

If you stopped the app and want to run it again:

**Windows:**
```bash
venv\Scripts\activate
python app.py
```

**macOS/Linux:**
```bash
source venv/bin/activate
python app.py
```

## Troubleshooting

### Error: "Python is not recognized"

Python is not in your PATH. Either:
- Reinstall Python and check "Add Python to PATH" during installation
- Use full path: `C:\Python311\python.exe app.py`

### Error: "No module named 'flask'"

Make sure you're in the virtual environment and installed dependencies:
```bash
# Activate venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

### Error: "Address already in use"

Another app is using port 5000. Either:
1. Close the conflicting app
2. Kill the process on port 5000:
   - **Windows**: `netstat -ano | findstr :5000` then `taskkill /PID <PID>`
   - **macOS/Linux**: `lsof -i :5000` then `kill -9 <PID>`

### Search returns zero results

- Make sure you're connected to the internet
- Try a simpler keyword like "construct"
- Click "Pre-load Cache" to ensure data is loaded

### Slow searches even after caching

- Give it a few seconds for cache to fully load
- Refresh the page if needed
- Try searching again

## Customizing the Application

### Change Search Port

Edit `app.py` and find the last line:
```python
if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

Change `5000` to another port like `8080`:
```python
app.run(debug=True, port=8080)
```

Then restart the app.

### Modify UI

Edit `templates/index.html` to change:
- Colors (search for `#667eea`)
- Text and labels
- Layout and styling

Refresh your browser to see changes (Ctrl+R or Cmd+R).

### Adjust Search Logic

Edit the `/api/search` endpoint in `app.py` to:
- Change how keywords are matched
- Filter results differently
- Add new search features

## Project Structure

```
codeforces-problem-search/
├── app.py                  # Main Flask application
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Web UI
├── README.md             # Project overview
├── LOCAL_SETUP.md        # This file
└── .git/                 # Git repository
```

## Development Tips

### Enable Debug Mode

The app runs in debug mode by default, which:
- Auto-reloads on file changes
- Shows detailed error messages
- Activates the interactive debugger

To disable, change `debug=True` to `debug=False` in `app.py`.

### View API Responses

Use a tool like Postman or curl to test API endpoints:

```bash
curl -X POST http://localhost:5000/api/search \
  -H "Content-Type: application/json" \
  -d '{"keywords":"construct","match_all":false}'
```

### Check Cache Status

Visit in your browser:
```
http://localhost:5000/api/cache-status
```

Should show:
```json
{"cached": true, "count": 10867}
```

## Performance Notes

- **Memory usage**: ~50-100 MB when running
- **Cache size**: ~1 MB in memory
- **Total problems**: 10,000+
- **First search**: 2-3 seconds
- **Cached searches**: <100ms

## Need Help?

1. Check the **README.md** for project overview
2. Check inline comments in `app.py`
3. Check error messages in your terminal
4. Create an issue on GitHub

## Next Steps

- Explore the codebase in `app.py` and `templates/index.html`
- Try modifying the UI or search logic
- Share your improvements!

---

**Happy coding!** 🚀
