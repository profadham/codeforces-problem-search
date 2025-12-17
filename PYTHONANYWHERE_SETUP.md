# PythonAnywhere Deployment Guide

## Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Create repository: `codeforces-problem-search`
3. **IMPORTANT**: Do NOT check any initialization options
4. Click "Create repository"
5. Run these commands to push your code:

```bash
cd d:\colledge\cp_new_page
git push -u origin main
```

When prompted for password, use your GitHub Personal Access Token (keep it secret!)

---

## Step 2: PythonAnywhere Setup (EASY!)

### 2.1 Sign up for PythonAnywhere

1. Go to https://www.pythonanywhere.com
2. Click "Sign up"
3. Choose a free account
4. Complete registration

### 2.2 Create a Web App in PythonAnywhere

1. Log in to PythonAnywhere
2. Click "Web" tab
3. Click "+ Add a new web app"
4. Choose framework: **Flask**
5. Choose Python version: **3.10** (or latest available)
6. Click through the setup

You'll now be in the Web app configuration page.

### 2.3 Clone Your Repository

1. Go to "Consoles" tab
2. Click "Bash" to open a terminal
3. Run these commands:

```bash
cd ~
git clone https://github.com/profadham/codeforces-problem-search.git
cd codeforces-problem-search
```

When prompted for password, use your token.

### 2.4 Create Virtual Environment

In the Bash console, run:

```bash
mkvirtualenv --python=/usr/bin/python3.10 codeforces
pip install -r requirements.txt
```

(Replace 3.10 with your chosen Python version)

### 2.5 Configure Flask App

1. Go back to "Web" tab
2. Under "Source code", set:
   - **Source code**: `/home/YOUR_USERNAME/codeforces-problem-search`
   - **Working directory**: `/home/YOUR_USERNAME/codeforces-problem-search`

Replace `YOUR_USERNAME` with your PythonAnywhere username (visible in top-right)

### 2.6 Configure WSGI File

1. Still in "Web" tab, find "WSGI configuration file"
2. Click on the WSGI file link (should be something like `/var/www/youruser_pythonanywhere_com_wsgi.py`)
3. Replace the entire contents with:

```python
import sys
import os

# Add your project directory to the path
path = os.path.expanduser('~') + '/codeforces-problem-search'
if path not in sys.path:
    sys.path.append(path)

# Activate virtual environment
activate_this = os.path.expanduser('~') + '/.virtualenvs/codeforces/bin/activate_this.py'
exec(open(activate_this).read(), {'__file__': activate_this})

from app import app as application
```

4. Click "Save"

### 2.7 Set Environment Variables (Optional)

1. In "Web" tab, scroll to "Environment variables"
2. Add:
   - Key: `FLASK_ENV`, Value: `production`
   - Key: `DEBUG`, Value: `False`

### 2.8 Reload Your Web App

1. At the top of the "Web" tab, click the green "Reload [yoursite.pythonanywhere.com]" button
2. Wait 5-10 seconds
3. Visit your web app URL!

Your app should now be live at: `https://youruser.pythonanywhere.com`

---

## Step 3: Verify It's Working

1. Visit your PythonAnywhere URL
2. Try searching for "construct"
3. Click "Pre-load Cache" to cache all problems
4. Share your URL with others!

---

## Troubleshooting

### Error: "Module not found"

- Check virtual environment is activated
- Run: `pip install -r requirements.txt` in Bash console
- Reload web app

### Error: "No module named 'flask'"

- Activate virtualenv: `source ~/.virtualenvs/codeforces/bin/activate`
- Install: `pip install flask`
- Reload web app

### Error: "Connection refused"

- Check Codeforces API is accessible from PythonAnywhere
- Try accessing https://codeforces.com/api/problemset.problems in browser

### White screen / 500 error

- Check error log: "Web" tab → "Error log"
- Look for clues in log file
- Reload web app

### Slow first search

- Click "Pre-load Cache" button to cache all problems
- Subsequent searches will be instant

---

## Updating Your App

To push updates to your live site:

1. Make changes locally
2. Commit and push to GitHub:

```bash
git add .
git commit -m "Your changes"
git push origin main
```

3. In PythonAnywhere Bash console:

```bash
cd ~/codeforces-problem-search
git pull origin main
```

4. Reload web app in "Web" tab

---

## Custom Domain (Optional)

To use a custom domain:

1. Go to "Web" tab
2. Scroll to "Domains"
3. Click "Add a new domain"
4. Follow instructions

---

## Questions?

- Check PythonAnywhere docs: https://help.pythonanywhere.com
- Check Flask docs: https://flask.palletsprojects.com
- Create an issue on GitHub

Good luck! 🚀
