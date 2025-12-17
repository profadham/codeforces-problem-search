# Contributing Guide

Thank you for your interest in contributing to the Codeforces Problem Search project! 🎉

## What Can You Contribute?

- 🐛 **Bug reports** - Found a bug? Let us know!
- ✨ **Features** - Have an idea for improvement?
- 📚 **Documentation** - Improve README or guides
- 🎨 **UI/UX improvements** - Better styling or interface
- ⚡ **Performance improvements** - Make it faster
- 🧪 **Tests** - Help improve code coverage

## Getting Started

### 1. Fork the Repository

Click the "Fork" button on GitHub to create your own copy.

### 2. Clone Your Fork

```bash
git clone https://github.com/YOUR_USERNAME/codeforces-problem-search.git
cd codeforces-problem-search
```

### 3. Create a Branch

```bash
git checkout -b feature/your-feature-name
```

Use descriptive branch names:
- `feature/better-search-algorithm`
- `fix/cache-not-loading`
- `docs/improve-readme`
- `ui/dark-mode`

### 4. Make Your Changes

Edit files and test locally. Remember to:
- Test your changes thoroughly
- Keep code clean and readable
- Add comments for complex logic
- Follow PEP 8 style guide (Python)

### 5. Commit Your Work

```bash
git add .
git commit -m "Clear description of what you changed"
```

Good commit messages:
- ✅ `Add keyword highlighting in search results`
- ✅ `Fix cache loading on refresh`
- ✅ `Improve mobile responsiveness`
- ❌ `fixed stuff`
- ❌ `update`

### 6. Push to Your Fork

```bash
git push origin feature/your-feature-name
```

### 7. Create a Pull Request

1. Go to the original repository on GitHub
2. Click "Pull requests" tab
3. Click "New pull request"
4. Select your fork and branch
5. Fill in description
6. Click "Create pull request"

## Code Style Guide

### Python (app.py, config.py)

Follow PEP 8:
```python
# Good
def search_problems(keywords, match_all=False):
    """Search for problems by keywords."""
    results = []
    for problem in problems:
        if matches(problem, keywords, match_all):
            results.append(problem)
    return results

# Bad
def search_problems(keywords,match_all=False):
    results=[]
    for p in problems:
        if matches(p,keywords,match_all):results.append(p)
    return results
```

### HTML/CSS (templates/index.html)

- Use semantic HTML
- Indent with 2 spaces
- Use meaningful class names
- Keep CSS organized by component

```html
<!-- Good -->
<div class="search-container">
    <input class="search-input" type="text">
    <button class="search-button">Search</button>
</div>

<!-- Bad -->
<div class="container">
    <input style="padding: 10px" type="text">
    <button onclick="search()">Go</button>
</div>
```

### JavaScript (templates/index.html)

- Use meaningful variable names
- Add comments for complex logic
- Use arrow functions when appropriate
- Avoid globals when possible

## Testing Your Changes

### Local Testing

Before submitting, always test locally:

```bash
# Activate virtual environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Run the app
python app.py

# Test in browser
# http://localhost:5000
```

### Test Checklist

- [ ] App starts without errors
- [ ] UI looks correct (desktop and mobile)
- [ ] Search functionality works
- [ ] Pre-load cache works
- [ ] No console errors in browser (F12)
- [ ] Related features still work

## Documentation Changes

If you edit README.md or create new docs:

- Use clear, simple language
- Add examples where helpful
- Keep formatting consistent
- Update table of contents if adding sections

## Feature Ideas

Want to contribute but not sure what? Here are some ideas:

- **Advanced search** - Regular expressions, exact match
- **Problem recommendations** - Suggest similar problems
- **Favorites** - Save favorite problems (local storage)
- **Statistics** - Show problem difficulty, acceptance rate
- **API improvements** - Cache problems locally
- **Tests** - Unit tests for search logic
- **Dark mode** - Theme toggle
- **Export** - Download search results as PDF/CSV

## Reporting Bugs

Found a bug? Create an issue with:

1. **Clear description** - What's broken?
2. **Steps to reproduce** - How to trigger it?
3. **Expected behavior** - What should happen?
4. **Actual behavior** - What actually happens?
5. **Screenshots** - If applicable
6. **System info** - Python version, OS, browser

Example:
```
Title: Search button doesn't work on Safari

Description:
When I search for "construct" on Safari, nothing happens. 
No results appear and no error messages show.

Steps to reproduce:
1. Open app on Safari
2. Type "construct" in search box
3. Click Search button
4. Nothing happens

Expected: 
Should show list of construction problems

Actual:
Page stays the same, no results

System:
- macOS 12.6
- Safari 16.1
- Python 3.11
```

## Code Review

When your PR is reviewed, be open to feedback:

- 👍 Feedback helps improve code quality
- 💬 Ask questions if something isn't clear
- 🔄 Be willing to make changes
- 📚 Reviewers might suggest better approaches

## Development Setup

To set up for development:

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/codeforces-problem-search.git
cd codeforces-problem-search

# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run in debug mode
python app.py
```

Now you can edit files and see changes live (auto-reload is enabled).

## File Guidelines

### app.py

- Keep endpoints organized
- Add docstrings to functions
- Comment on complex logic
- Don't hardcode configuration

### templates/index.html

- Keep markup semantic
- Separate CSS in `<style>` tags
- Separate JavaScript in `<script>` tags
- Use data attributes for dynamic content

### requirements.txt

- Pin versions for stability
- Add new dependencies as needed
- Keep list minimal

## Performance Considerations

When making changes, consider:

- **Memory usage** - Cache size, large arrays
- **Speed** - Search performance, API calls
- **Responsiveness** - Don't block UI
- **Caching** - Use appropriate cache strategies

## Commit Frequently

Make small, focused commits:

```bash
# Good
git commit -m "Add search result caching"
git commit -m "Improve mobile responsiveness"
git commit -m "Fix CSS color bug"

# Avoid
git commit -m "Multiple changes to search, UI, and config"
```

## Before Submitting

- [ ] Code follows style guide
- [ ] Tests pass locally
- [ ] No console errors
- [ ] Documentation updated if needed
- [ ] Commit messages are clear
- [ ] Branch is up to date with main

## Getting Help

- 💬 Ask questions in issues
- 📖 Read existing documentation
- 🔍 Look at similar code for examples
- 👥 Comment on related PRs

## Code of Conduct

- Be respectful
- Be inclusive
- Give credit
- Provide constructive feedback
- No spam or self-promotion

## Thank You! 🙏

Every contribution, no matter how small, helps make this project better!

---

Questions? Open an issue or create a discussion on GitHub!
