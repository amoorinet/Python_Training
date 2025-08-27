[⬅ Back to Main README](../README.md)

# Git: Core Concepts & Flow

**Local actions on your PC**  
- `git add .` → stage all changed files (mark them for commit).  
- `git commit -m "msg"` → save a snapshot into your **local** Git history.  
- `git push` → upload local commits to **GitHub (remote)**.  

**Get updates from GitHub**  
- `git fetch` → download new commits into `origin/<branch>` **without** changing your files yet.  
- `git pull` → `fetch + merge` → apply GitHub’s new commits to your local branch and update your files.  

---

## ✅ Remember the direction

- `add → commit → push` = go **upwards** (PC → GitHub)  
- `fetch → pull` = go **downwards** (GitHub → PC)

---

# 🔹 Git Flow Diagram (Local ↔ Remote)

```mermaid
flowchart TD
    A[Your Working Folder on PC] -->|git add .| B[Staging Area (local index)]
    B -->|git commit -m "msg"| C[Local Git Repository (history on your PC)]
    C -->|git push| D[Remote Repository (GitHub)]
```

# 🔹 Getting Updates from GitHub

```mermaid
flowchart TD
    D[Remote Repository (GitHub)] -->|git fetch| E[Remote Tracking Branch (origin/main)]
    E -->|git pull (fetch + merge)| C[Local Git Repository + Working Folder updated]
```

---

# 📘 Create & Publish a New Repository on GitHub

This cheat sheet summarizes four common methods to create a repo, commit files, push them to GitHub, and later pull or fetch updates.

---

## 1) Plain Git CLI (PowerShell on Windows)

```powershell
# Create new project folder
mkdir -Force "C:\python\new_project"
cd "C:\python\new_project"

# Initialize project
'\# my-project' | Out-File -Encoding utf8 README.md   # or: echo "# my-project" > README.md
git init
git add .
git commit -m "first commit"
git branch -M main

# Connect to GitHub repo (replace URL with yours)
git remote add origin https://github.com/USERNAME/REPO.git

# Push for the first time
git push -u origin main

# Later usage
git pull origin main    # bring latest updates into your local branch
git fetch origin        # check/download updates without merging
```

---

## 2) GitHub CLI (`gh`)

```powershell
# Authenticate GitHub CLI (interactive)
gh auth login

# Create project folder
mkdir -Force "C:\python\new_project"
cd "C:\python\new_project"

# Add a sample file
'print("hello")' | Out-File -Encoding utf8 app.py

# Initialize repository
git init
git add .
git commit -m "initial commit"
git branch -M main

# Create + push repo in one command
gh repo create REPO_NAME --public --source=. --remote=origin --push

# Later usage
git pull    # get updates (fetch + merge)
git fetch   # only check/download updates
```

---

## 3) GitHub Desktop (GUI)

1. **File → New Repository** → enter **Name** and **Local path** → check **Initialize with README**.  
2. Click **Create Repository**.  
3. Click **Publish Repository** (choose **Public** or **Private**).  
4. Use **Fetch origin** to check for updates.  
5. Use **Pull origin** to bring updates into your local repo.

---

## 4) VS Code (Insiders / Stable)

1. **File → Open Folder…** → select your project folder.  
2. Go to **Source Control** (left sidebar) → **Initialize Repository**.  
3. Stage changes (**+**), write a commit message, click **✔ Commit**.  
4. Click **Publish Branch** to push to GitHub.  
5. Later: **Pull** to update; **Command Palette → Git: Fetch** to only check for updates.

---

## ✅ Quick Check (view your history graph)

```bash
git log --oneline --decorate --graph --all
```

---

## ✅ Add, Commit, Publish (any time)

```bash
git add .
git commit -m "your message"
git remote -v
git push
git status
```

---

## 🔁 Example Run (PowerShell prompt sample)

```text
(venv) PS C:\Python\BARAA\Python_Barra\python scripts\Copilot\Python_Training>
```

```powershell
git add .
git commit -m "link README.md to all .txt files"
git remote -v
git push
git status
```

**What happens**  
- `git add .` → stage all changes  
- `git commit -m` → save snapshot with a message  
- `git remote -v` → confirm the remote repo URL(s)  
- `git push` → upload commits to GitHub  
- `git status` → show current repo status

---

## ℹ️ Glossary (super short)
- **Working folder**: Your files on disk.  
- **Staging area**: Files selected for the next commit.  
- **Commit**: A saved snapshot in Git history.  
- **Remote**: The GitHub copy of your repository.  
- **Branch**: A line of development (e.g., `main`, `dev`).

