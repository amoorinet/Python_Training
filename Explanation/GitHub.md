[⬅ Back to Main README](../README.md)
📘 How to Create and Publish a New Repository on GitHub

This cheat sheet summarizes four methods to create a repository, commit files, push them to GitHub, and later pull or fetch updates.

1. Plain Git CLI
# Create new project folder
mkdir -Force "C:\python\new_project"
cd "C:\python\new_project"

# Initialize project
echo "# my-project" > README.md
git init
git add .
git commit -m "first commit"
git branch -M main

# Connect to GitHub repo (replace URL with yours)
git remote add origin https://github.com/amoorinet/repo.git

# Push for the first time
git push -u origin main

# Later usage
git pull origin main    # bring latest updates
git fetch origin        # check updates without merging

2. GitHub CLI (gh)
# Authenticate GitHub CLI
gh auth login

# Create project folder
mkdir -Force "C:\python\new_project"
cd "C:\python\new_project"

# Add a sample file
echo "print('hello')" > app.py

# Initialize repository
git init
git add .
git commit -m "commit all"
git branch -M main

# Create + push repo in one command
gh repo create repo_name --public --source=. --remote=origin --push

# Later usage
git pull    # get updates
git fetch   # check updates only

3. GitHub Desktop (GUI)

Open GitHub Desktop → File → New Repository

Fill in details (Name, Local path, etc.), check Initialize with README

Click Create Repository

To publish online → click Publish Repository (choose public/private)

Use Fetch origin to check updates

Use Pull origin to bring updates

4. VS Code (Insiders / Stable)

Open VS Code → File → Open Folder → select your project folder

Go to Source Control tab (left sidebar)

Click Initialize Repository

Stage changes (+), write a commit message, then click ✓ Commit

Click Publish Branch (to push repo to GitHub)

Later:

Pull → to update

Command Palette → Git: Fetch → only check updates

✅ Quick Check

Verify commits visually:

git log --oneline --decorate --graph --all

✅ Tips to Add, Commit, and Publish

When you’re ready to save and publish changes:

git add .
git commit -m "your message"
git remote -v
git push
git status

Example Run

If your terminal path looks like:

(venv) PS C:\Python\BARAA\Python_Barra\python scripts\Copilot\Python_Training>


Paste commands:

git add .
git commit -m "test to link README.md to all .txt file"
git remote -v
git push
git status

What happens

git add . → Stage all changes

git commit -m → Save snapshot with a message

git remote -v → Confirm remote repo

git push → Upload commits to GitHub

git status → Show repo status

👉 Tip: You can run them step by step or paste all at once

