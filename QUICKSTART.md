# 🚀 DEPLOYMENT INSTRUCTIONS

## Your GitHub Details
- **Username**: profadham
- **Repository**: codeforces-problem-search
- **GitHub URL**: https://github.com/profadham/codeforces-problem-search

---

## STEP 1: Create GitHub Repository (5 minutes)

### 1.1 Create Repo on GitHub
1. Go to: https://github.com/new
2. Fill in:
   - **Repository name**: `codeforces-problem-search`
   - **Description**: Web app to search Codeforces problems by keywords
   - **Public** or **Private** (your choice)
3. **IMPORTANT**: Do NOT check:
   - ☐ Add a README file
   - ☐ Add .gitignore
   - ☐ Choose a license
4. Click **"Create repository"**

### 1.2 Push Your Code
Once repository is created, run these commands in PowerShell:

```powershell
cd d:\colledge\cp_new_page
git push -u origin main
```

When prompted:
- **Username**: profadham
- **Password**: Use this token: `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`

After push succeeds, verify at: https://github.com/profadham/codeforces-problem-search

---

## STEP 2: Deploy to PythonAnywhere (10-15 minutes)

### 2.1 Sign Up
Go to: https://www.pythonanywhere.com → Sign up (free account)

### 2.2 Create Web App
1. Log in
2. Click **"Web"** tab (top menu)
3. Click **"+ Add a new web app"**
4. Choose:
   - Framework: **Flask**
   - Python: **3.10** (or latest)
5. Complete the setup

### 2.3 Clone Repository (in PythonAnywhere)
1. Click **"Consoles"** tab
2. Click **"Bash"** button
3. Run:
```bash
cd ~
git clone https://github.com/profadham/codeforces-problem-search.git
cd codeforces-problem-search
```

### 2.4 Install Dependencies
In Bash console, run:
```bash
mkvirtualenv --python=/usr/bin/python3.10 codeforces
pip install -r requirements.txt
```

(Note: mkvirtualenv activates the virtualenv automatically)

### 2.5 Configure Web App
1. Go back to **"Web"** tab
2. Scroll down to **"Source code"** section
3. Set:
   - **Source code**: `/home/YOUR_USERNAME/codeforces-problem-search`
   - **Working directory**: `/home/YOUR_USERNAME/codeforces-problem-search`
   
   (Find YOUR_USERNAME in top-right corner of PythonAnywhere)

### 2.6 Configure WSGI File
1. In **"Web"** tab, find **"WSGI configuration file"**
2. Click the file path link (looks like `/var/www/something_wsgi.py`)
3. Delete all content and paste this:

```python
import sys
import os

path = os.path.expanduser('~') + '/codeforces-problem-search'
if path not in sys.path:
    sys.path.append(path)

activate_this = os.path.expanduser('~') + '/.virtualenvs/codeforces/bin/activate_this.py'
exec(open(activate_this).read(), {'__file__': activate_this})

from app import app as application
```

4. Click **"Save"**

### 2.7 Reload & Launch!
1. Go to **"Web"** tab
2. Click the green **"Reload"** button at top
3. Wait 5-10 seconds
4. Click your web app URL (bottom of page) or visit:
   ```
   https://YOUR_USERNAME.pythonanywhere.com
   ```

---

## ✅ DONE! Your App is Live!

Your Codeforces Problem Search is now deployed and accessible online!

### What to do next:
1. **Test it**: Visit your PythonAnywhere URL
2. **Try a search**: Search for "construct"
3. **Pre-load cache**: Click "Pre-load Cache" for instant future searches
4. **Share the URL**: Send it to friends/classmates!

---

## 🔧 Updating Your App

Want to make changes and update the live version?

1. Edit files locally in VS Code
2. Commit and push:
   ```bash
   cd d:\colledge\cp_new_page
   git add .
   git commit -m "Your change description"
   git push origin main
   ```
3. In PythonAnywhere Bash console:
   ```bash
   cd ~/codeforces-problem-search
   git pull origin main
   ```
4. In **"Web"** tab, click **"Reload"** button

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| "Module not found" | Click **"Consoles"** → **"Bash"**, run `pip install -r requirements.txt` |
| White screen / 500 error | Check error log in **"Web"** tab → **"Error log"** |
| Slow first search | Click "Pre-load Cache" button in the app |
| Can't clone repo | Make sure token has correct permissions |
| WSGI file not working | Edit it again, clear spaces, copy-paste code exactly |

---

## 📖 Full Documentation

- **General Deployment**: See `DEPLOYMENT.md`
- **Detailed PythonAnywhere**: See `PYTHONANYWHERE_SETUP.md`
- **Local Development**: See `README.md`

---

**Questions?** Check PythonAnywhere docs: https://help.pythonanywhere.com

Good luck! 🚀
