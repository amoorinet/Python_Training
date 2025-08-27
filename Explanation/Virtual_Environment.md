[⬅ Back to Main README](../README.md)

# Python Virtual Environment Setup Guide for Windows 11

## PowerShell Execution Policy Setup

### Command
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
cd "C:\Python\BARAA\Python_Barra\python scripts"

Explanation
Execution Policy → In Windows PowerShell, this controls whether scripts are allowed to run (for security)

RemoteSigned → This level means:

Scripts written on your computer can run without restriction

Scripts downloaded from the internet must be signed by a trusted publisher

Scope Process → This applies only to the current PowerShell session (once you close the window, it resets)

Conclusion
👉 "For this PowerShell window, allow me to run my local scripts without restriction, but keep some security checks for downloaded scripts."

⚡ Why Needed for Virtual Environment
When you create or activate a Python virtual environment (venv), PowerShell runs a small script called Activate.ps1.

By default, Windows blocks running .ps1 scripts for security.

That's why you sometimes see errors like:

text
running scripts is disabled on this system
To fix this temporarily, you run:

powershell
Set-ExecutionPolicy RemoteSigned -Scope Process
This tells PowerShell:
✅ "Let me run activation scripts (Activate.ps1) just for this session."

📝 Notes
You don't always need it — only if PowerShell blocks your venv activation

It's safe when used with -Scope Process because it applies only to your current PowerShell window, not system-wide

How to Create and Activate Virtual Environment
Step 1: Go to your project folder
powershell
cd "C:\Python\BARAA\Python_Barra\python scripts\Copilot\Python_Training"
Step 2: Create a virtual environment
powershell
python -m venv venv
What this does:

Creates a new folder called venv inside your project

Contains its own Python interpreter and libraries (separate from your system Python)

Step 3: Activate the virtual environment
powershell
.\venv\Scripts\Activate
After activation, you should see (venv) at the start of your prompt:

text
(venv) PS C:\Python\BARAA\Python_Barra\python scripts\Copilot\Python_Training>
The (venv) appears in a different color, indicating you're now working inside your isolated Python environment.

Step 4: Deactivate (when done)
To go back to your global Python:

powershell
deactivate
Additional Virtual Environment Commands
Install packages in virtual environment
powershell
pip install package-name
List installed packages
powershell
pip list
Freeze requirements to file
powershell
pip freeze > requirements.txt
Install from requirements file
powershell
pip install -r requirements.txt
Troubleshooting Common Issues
If activation fails:
powershell
# Try using the full path
C:\Path\To\Your\venv\Scripts\Activate.ps1
If you get permission errors:
powershell
# Run PowerShell as Administrator first
Alternative activation method (Command Prompt):
cmd
venv\Scripts\activate.bat
Best Practices
Always use virtual environments for Python projects

Keep your requirements.txt file updated

Never run production code in the global Python environment

Use different virtual environments for different projects

