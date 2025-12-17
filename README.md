# Codeforces Problem Search

A web application to search for Codeforces problems by keywords in problem names and tags.

## Features

- 🔍 Search problems by keywords
- ✓ Match ANY (OR) or ALL (AND) keywords
- 💾 Problem caching for faster subsequent searches
- 🎨 Beautiful, responsive web UI
- ⚡ Fast API integration with Codeforces

## Setup

### Prerequisites
- Python 3.8+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/codeforces-problem-search.git
cd codeforces-problem-search
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to `http://localhost:5000`

## Usage

1. Enter keywords separated by spaces (e.g., "construct permutation")
2. Optionally check "Match ALL" to find problems with all keywords (default is ANY)
3. Click Search or press Enter
4. Click "Pre-load Cache" for instant searches on first use

## API Reference

### POST /api/search
Search for problems by keywords

**Request:**
```json
{
  "keywords": "construct permutation",
  "match_all": false
}
```

**Response:**
```json
{
  "status": "success",
  "count": 100,
  "results": [
    {
      "link": "https://codeforces.com/problemset/problem/...",
      "name": "Problem Name",
      "tags": ["tag1", "tag2"],
      "contestId": 1234,
      "index": "A"
    }
  ]
}
```

### POST /api/load-cache
Pre-load all Codeforces problems into memory

### GET /api/cache-status
Check if problems are cached and get total count

## Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for instructions on deploying to:
- Heroku
- PythonAnywhere
- Render
- AWS

## File Structure

```
.
├── app.py                 # Flask application
├── templates/
│   └── index.html        # Web UI
├── requirements.txt      # Python dependencies
├── README.md            # This file
└── DEPLOYMENT.md        # Deployment guide
```

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **API**: Codeforces API
- **Deployment**: Various options

## License

MIT License

## Author

Your Name

## Contributing

Pull requests are welcome!
