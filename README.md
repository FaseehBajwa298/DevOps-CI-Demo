# DevOps-CI-Demo

Simple Python app to demonstrate creating a GitHub repository and pushing code.

## Prerequisites
- Python 3.8+
- Git
- (Optional) GitHub CLI `gh` for easy repo creation and pushing

## Run the app

```bash
python app.py
```

### Run with a custom name

```bash
python app.py --name "Faseeh"
```

## Initialize Git and push to GitHub (recommended via GitHub CLI)

```bash
git init
git add .
git branch -M main
git commit -m "Initial commit: simple Python app"

# Create the GitHub repo and push in one step
gh repo create DevOps-CI-Demo --public --source . --remote origin --push --confirm
```

## Alternative: Manual GitHub setup
If you prefer the web UI:
1. Go to https://github.com/new and create a repository named `DevOps-CI-Demo`.
2. Do not add a README/license (we already have one locally).
3. Then run:

```bash
git remote add origin https://github.com/<your-username>/DevOps-CI-Demo.git
git push -u origin main
```

## Notes
- Update your local Git identity if needed:
  ```bash
  git config user.name "Your Name"
  git config user.email "you@example.com"
  ```
- If `gh` isn’t installed: `winget install --id GitHub.cli -e --accept-source-agreements --accept-package-agreements`