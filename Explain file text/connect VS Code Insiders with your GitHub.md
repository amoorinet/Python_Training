🚀 Git & GitHub Quickstart (with VS Code Insiders)
0) Prerequisites (one time)

Install Git → check with:

git --version


Sign in GitHub in VS Code Insiders
Bottom-left Accounts → Sign in to GitHub → Authorize.

1) Clone your repository

VS Code Insiders → Ctrl+Shift+P → Git: Clone

Paste your repo URL (must end with .git):

https://github.com/amoorinet/trraning.git


Pick a local folder → when prompted, click Open.

2) Set your Git identity (authorship)

Do this once per machine:

git config --global user.name "amoorinet"
git config --global user.email "your_email@example.com"


💡 For privacy: use your GitHub noreply email (GitHub → Settings → Emails).

3) Add your project files

Copy your Python files from your working folder
(e.g. C:\Python\BARAA\Python_Barra\python scripts\...)

Paste them inside the cloned trraning folder.

4) Add a .gitignore (to keep repo clean)

Create a file named .gitignore in the repo:

# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.env
.venv
venv/
ENV/
env/
*.egg-info/
dist/
build/

# VS Code
.vscode/

# OS junk
.DS_Store
Thumbs.db

5) First commit & push (with VS Code GUI)

Open Source Control (branch icon).

Click + (Stage All).

Enter message:

first commit: add training scripts


Click Commit (✓).

Click Push (↑).

✅ Now your files are on GitHub.

6) Verify

Open in browser:

https://github.com/amoorinet/trraning


You should see your files.

📝 Daily Workflow (Cheat Sheet)

Pull latest → git pull

Stage all → git add .

Commit → git commit -m "message"

Push → git push

Status → git status

💡 You can stage many files and commit with one message.

🔄 Alternative: connect existing folder

If you already have a project folder and want to link it to GitHub:

cd "C:\Path\To\Your\Existing\Folder"
git init
git add .
git commit -m "initial commit"
git branch -M main
git remote add origin https://github.com/amoorinet/trraning.git
git push -u origin main


Then open this folder in VS Code Insiders.

🐍 Virtual Environment Note

Create/activate a venv in the repo if needed:

python -m venv venv
.\venv\Scripts\activate


The .gitignore already excludes venv/ so your repo stays clean.