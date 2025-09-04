import tkinter as tk
from tkinter import ttk
import sys


class PowerShellFixer:
    def __init__(self, root):
        self.root = root
        self.root.title("PowerShell Execution Policy Fixer")
        self.root.geometry("700x500")
        self.root.configure(bg="#2b2b2b")

        # Create style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TFrame', background='#2b2b2b')
        style.configure('TLabel', background='#2b2b2b', foreground='white')
        style.configure('Header.TLabel', font=('Arial', 14, 'bold'))
        style.configure('TButton', background='#4CAF50', foreground='black')
        style.configure('Fixed.TLabel', font=('Consolas', 10),
                        background='#3c3c3c', foreground='white')
        style.configure('TRadiobutton', background='#2b2b2b',
                        foreground='white')

        # Header
        header = ttk.Label(
            root, text="PowerShell Execution Policy Error Fix", style='Header.TLabel')
        header.pack(pady=20)

        # Explanation
        explanation = ttk.Frame(root)
        explanation.pack(pady=10, padx=20, fill='x')

        text = """Your error: PowerShell is preventing script execution due to security policies.

This happens because:
1. PowerShell has a security feature called "Execution Policy"
2. By default, it's set to "Restricted" which blocks all scripts
3. The mmdc command you tried to run is a PowerShell script

Solution: Change the execution policy to allow running scripts."""

        explanation_label = ttk.Label(
            explanation, text=text, wraplength=650, justify='left')
        explanation_label.pack()

        # Policy options
        policy_frame = ttk.LabelFrame(root, text="Select Execution Policy")
        policy_frame.pack(pady=20, padx=20, fill='x')

        self.policy_var = tk.StringVar(value="RemoteSigned")

        policies = [
            ("Restricted (Default) - No scripts allowed", "Restricted"),
            ("AllSigned - Only signed scripts", "AllSigned"),
            ("RemoteSigned - Downloaded scripts must be signed", "RemoteSigned"),
            ("Unrestricted - All scripts allowed (not recommended)", "Unrestricted"),
            ("Bypass - Nothing is blocked (not recommended)", "Bypass")
        ]

        for text, mode in policies:
            rb = ttk.Radiobutton(policy_frame, text=text,
                                 variable=self.policy_var, value=mode)
            rb.pack(anchor='w', padx=10, pady=5)

        # Recommended option
        rec_label = ttk.Label(
            policy_frame, text="Recommended: RemoteSigned", foreground="#4CAF50")
        rec_label.pack(anchor='w', padx=10, pady=5)

        # Buttons
        button_frame = ttk.Frame(root)
        button_frame.pack(pady=20)

        ttk.Button(button_frame, text="Apply Fix",
                   command=self.apply_fix).pack(side='left', padx=10)
        ttk.Button(button_frame, text="Show Current Policy",
                   command=self.show_policy).pack(side='left', padx=10)
        ttk.Button(button_frame, text="Test mmdc Command",
                   command=self.test_mmdc).pack(side='left', padx=10)

        # Output area
        output_frame = ttk.LabelFrame(root, text="Command Output")
        output_frame.pack(pady=10, padx=20, fill='both', expand=True)

        self.output_text = tk.Text(
            output_frame, height=10, bg="#3c3c3c", fg="white", font=("Consolas", 10))
        scrollbar = ttk.Scrollbar(
            output_frame, orient='vertical', command=self.output_text.yview)
        self.output_text.configure(yscrollcommand=scrollbar.set)

        self.output_text.pack(side='left', fill='both',
                              expand=True, padx=5, pady=5)
        scrollbar.pack(side='right', fill='y', pady=5)

        # Add initial message
        self.output_text.insert(
            'end', "Ready to fix PowerShell execution policy issues...\n")
        self.output_text.config(state='disabled')

    def run_powershell_command(self, command):
        """Run a PowerShell command and return the output"""
        try:
            result = subprocess.run([
                'powershell', '-Command', command
            ], capture_output=True, text=True, timeout=30)

            return result.stdout, result.stderr, result.returncode
        except Exception as e:
            return "", str(e), -1

    def apply_fix(self):
        """Apply the selected execution policy"""
        policy = self.policy_var.get()
        command = f"Set-ExecutionPolicy {policy} -Scope CurrentUser -Force"

        self.output_text.config(state='normal')
        self.output_text.delete(1.0, 'end')
        self.output_text.insert('end', f"Running: {command}\n")
        self.output_text.insert('end', "Please wait...\n")
        self.output_text.config(state='disabled')
        self.root.update()

        stdout, stderr, returncode = self.run_powershell_command(command)

        self.output_text.config(state='normal')
        self.output_text.insert('end', "="*50 + "\n")

        if returncode == 0:
            self.output_text.insert(
                'end', "✓ Execution policy updated successfully!\n")
            self.output_text.insert('end', f"New policy: {policy}\n")
        else:
            self.output_text.insert(
                'end', "✗ Failed to update execution policy\n")
            if stderr:
                self.output_text.insert('end', f"Error: {stderr}\n")

        self.output_text.config(state='disabled')

    def show_policy(self):
        """Show the current execution policy"""
        self.output_text.config(state='normal')
        self.output_text.delete(1.0, 'end')
        self.output_text.insert(
            'end', "Checking current execution policy...\n")
        self.output_text.config(state='disabled')
        self.root.update()

        stdout, stderr, returncode = self.run_powershell_command(
            "Get-ExecutionPolicy -List")

        self.output_text.config(state='normal')
        self.output_text.insert('end', "="*50 + "\n")
        self.output_text.insert('end', "Current Execution Policies:\n")

        if stdout:
            self.output_text.insert('end', stdout)
        if stderr:
            self.output_text.insert('end', f"Error: {stderr}\n")

        self.output_text.config(state='disabled')

    def test_mmdc(self):
        """Test if mmdc command works now"""
        self.output_text.config(state='normal')
        self.output_text.delete(1.0, 'end')
        self.output_text.insert('end', "Testing mmdc command...\n")
        self.output_text.config(state='disabled')
        self.root.update()

        # Try to get mmdc version
        stdout, stderr, returncode = self.run_powershell_command(
            "mmdc --version")

        self.output_text.config(state='normal')
        self.output_text.insert('end', "="*50 + "\n")

        if returncode == 0:
            self.output_text.insert('end', "✓ mmdc is working correctly!\n")
            self.output_text.insert('end', f"Version: {stdout}\n")
        else:
            self.output_text.insert('end', "✗ mmdc is not working yet\n")
            if "not recognized" in stderr:
                self.output_text.insert(
                    'end', "mmdc is not installed or not in PATH\n")
            else:
                self.output_text.insert('end', f"Error: {stderr}\n")

            self.output_text.insert('end', "\nTry these steps:\n")
            self.output_text.insert(
                'end', "1. Make sure Node.js is installed: https://nodejs.org/\n")
            self.output_text.insert(
                'end', "2. Install mermaid-cli: npm install -g @mermaid-js/mermaid-cli\n")
            self.output_text.insert(
                'end', "3. Restart PowerShell after installation\n")

        self.output_text.config(state='disabled')


if __name__ == "__main__":
    root = tk.Tk()
    app = PowerShellFixer(root)
    root.mainloop()
