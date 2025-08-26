[⬅ Back to Main README](../README.md)

# Pylint Warnings Cheat Sheet (Beginner-Friendly) 📑

## Common Warnings & Fixes

| Warning | What it Means | Simple Fix |
|---------|---------------|------------|
| **C0114**: missing-module-docstring | No description at the top of your script | Add `"""This script does XYZ."""` at the very top |
| **C0304**: missing-final-newline | Your file ends without a blank line | Just press Enter at the end once |
| **C0301**: line-too-long (xxx/100) | A line is longer than 100 characters | Split it into multiple lines using `\` or parentheses |
| **C0103**: invalid-name | Variable, function, or file doesn't follow Python naming style (snake_case) | Rename: `Class_Object_Method.py` → `class_object_method.py` |
| **W0611**: unused-import | You imported something but never used it | Delete the unused import |
| **W0612**: unused-variable | You created a variable but never used it | Remove or actually use it |
| **R1705**: unnecessary-else | You used an else after return | Remove else because code won't reach it anyway |
| **C0411**: wrong-import-order | Imports are not in the standard order | Group: built-ins → third-party → local imports |

## Python Naming Conventions & Pylint Errors

### 🐍 snake_case (functions, variables, files)
**Rule**: Must be lowercase with underscores.

**Pylint Error if broken**: `C0103: invalid-name`
- Example: `MyFunction` instead of `my_function`
- Example: `Class_Object_Method.py` instead of `class_object_method.py`

**✅ Fix**: rename to snake_case.

### 🐪 CamelCase (PascalCase in Python) (classes, exceptions)
**Rule**: Each word starts with uppercase, no underscores.

**Pylint Error if broken**: `C0103: invalid-name`
- Example: `villa_progress` instead of `VillaProgress` for a class

**✅ Fix**: rename class to CamelCase.

### 🔠 ALL_CAPS (constants)
**Rule**: Constants should be uppercase with underscores.

**Pylint Error if broken**: `C0103: invalid-name`
- Example: `pi = 3.14` instead of `PI = 3.14`

**✅ Fix**: rename constant to ALL_CAPS.

### 📜 Docstrings
**Rule**: Every module, class, and function should start with a docstring.

**Pylint Errors if broken**:
- `C0114: missing-module-docstring` → no description at top of file
- `C0115: missing-class-docstring` → no description inside a class
- `C0116: missing-function-docstring` → no description inside a function

**✅ Fix**: add a triple-quoted string `"""This does XYZ"""`.

### 🔚 Final newline
**Rule**: File should end with one blank line.

**Pylint Error if broken**: `C0304: missing-final-newline`

**✅ Fix**: add a newline at the very end of file.

## Quick Visual Table

| Item | Correct Style | Pylint Error if Broken | Example Fix |
|------|---------------|------------------------|-------------|
| Variable | `villa_count` | `C0103: invalid-name` | rename to snake_case |
| Function | `get_total()` | `C0103: invalid-name` | rename to snake_case |
| File name | `data_utils.py` | `C0103: invalid-name` | rename to snake_case |
| Class | `VillaProgress` | `C0103: invalid-name` | rename to CamelCase |
| Constant | `MAX_VILLAS` | `C0103: invalid-name` | rename to ALL_CAPS |
| Module docs | `"""Info..."""` | `C0114/15/16: missing-…` | add docstring |
| End of file | newline | `C0304: missing-final-newline` | add blank line |

## Understanding Variable Names in Python

### Variable Naming Flexibility
You can name variables however you like (as long as they follow the syntax rules):

```python
name = "Aamir"   # works
NAME = "Aamir"   # works  
Name = "Aamir"   # works
All are valid Python.

🔹 Why Pylint Complained About name
Pylint thought your variable was a constant (a value that shouldn't change, like PI = 3.14159).

PEP8 convention:

variables → snake_case → name, my_age, total_sum

constants → UPPER_CASE → PI, MAX_SIZE, DEFAULT_COLOR

classes → CamelCase → MyClass, Person

functions → snake_case → calculate_area()

When Pylint saw:


name = "Aamir Ahmed"
It assumed name should be a constant (UPPER_CASE), but you meant it as a variable.

That's why you got:


Constant name "name" doesn't conform to UPPER_CASE naming style
🔹 What to Do
✅ If it's a normal variable, keep it lowercase:


name = "Aamir Ahmed"   # correct for variables
✅ If it's really a constant:


PI = 3.14159
APP_NAME = "MyApp"
🔹 Two Easy Fixes
Ignore the warning → because your code works fine

Configure/disable that specific rule in .pylintrc if you don't like it:

ini
disable=C0103
(this disables the invalid-name check)

👉 So: You don't have to use all capitals for string variables. That's only for constants. Pylint just misclassified your name variable.