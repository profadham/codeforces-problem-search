# Deployment Guide

## Option 1: Heroku (Recommended for beginners)

### Prerequisites

- Heroku account (free tier available)
- Heroku CLI installed

### Steps

1. **Login to Heroku:**

```bash
heroku login
```

2. **Create a new app:**

```bash
heroku create your-app-name
```

3. **Create Procfile:**
   The `Procfile` tells Heroku how to run your app (already included in repo)

4. **Deploy:**

```bash
git push heroku main
```

5. **Open your app:**

```bash
heroku open
```

**Note:** Heroku's free tier was discontinued. Use alternatives below.

---

## Option 2: PythonAnywhere (Easiest - Free tier available)

### Steps

1. Go to [pythonanywhere.com](https://www.pythonanywhere.com) and sign up

2. Create a new web app:

   - Click "Add a new web app"
   - Choose "Flask"
   - Choose Python version 3.8+

3. Clone repo in Bash console:

```bash
cd /home/YOUR_USERNAME
git clone https://github.com/YOUR_USERNAME/codeforces-problem-search.git
```

4. Set up virtual environment:

```bash
mkvirtualenv --python=/usr/bin/python3.8 codeforces
pip install -r codeforces-problem-search/requirements.txt
```

5. Configure web app:

   - Go to Web tab
   - Set source code to: `/home/YOUR_USERNAME/codeforces-problem-search`
   - Set working directory to: `/home/YOUR_USERNAME/codeforces-problem-search`
   - Set WSGI configuration file

6. Edit WSGI file (in Web tab):

```python
import sys
path = '/home/YOUR_USERNAME/codeforces-problem-search'
if path not in sys.path:
    sys.path.append(path)

from app import app as application
```

7. Reload web app and visit your PythonAnywhere URL

---

## Option 3: Render (Free tier with limitations)

### Steps

1. Go to [render.com](https://render.com) and sign up

2. Click "New +" and select "Web Service"

3. Connect your GitHub repository

4. Configure:

   - **Name**: your-app-name
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`

5. Deploy!

---

## Option 4: Railway (Easy deployment)

### Steps

1. Go to [railway.app](https://railway.app) and sign up with GitHub

2. Click "Create New Project" → "Deploy from GitHub repo"

3. Select your repository

4. Railway auto-detects Flask and deploys automatically

---

## Option 5: Replit (Quick, Free)

### Steps

1. Go to [replit.com](https://replit.com) and sign up

2. Click "Create Repl" → "Import from GitHub"

3. Paste your repo URL

4. Replit auto-detects and runs your Flask app

5. Share your Replit URL with others

---

## Environment Variables

If needed, create a `.env` file (already in `.gitignore`):

```
FLASK_ENV=production
DEBUG=False
```

---

## Performance Tips

1. **Pre-load cache** on startup to avoid slow first searches
2. **Use a production WSGI server** like Gunicorn (not Flask's dev server)
3. **Consider caching** Codeforces API responses
4. **Monitor memory usage** if running on limited resources

---

## Troubleshooting

**"Module not found" error:**

```bash
pip install -r requirements.txt
```

**"Connection refused":**

- Check if Flask app is running
- Verify port 5000 is not blocked

**"API Error 403":**

- Check internet connection
- Codeforces API might be rate-limited; add delays

---

## Custom Domain

Most services allow mapping custom domains:

- PythonAnywhere: Web tab → Domains
- Render: Settings → Custom Domain
- Railway: Settings → Custom Domain

---

## Monitoring & Logs

- **PythonAnywhere**: Web tab → View logs
- **Render**: Dashboard → View logs
- **Railway**: View → Logs
- **Heroku**: `heroku logs --tail`
