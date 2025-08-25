# 📘 Python Reference Guide: Functions, Modules, Libraries, Classes & Built-ins

---

## 1.Functions in Python
A **function** is a reusable block of code that performs a specific task.

### 🔑 Key Features
- **Reusable** → avoids code duplication  
- **Modular** → improves readability  
- **Flexible** → can accept inputs (parameters) and return outputs  

### Structure
```python
def greet(name):          # Definition
    return f"Hello, {name}!"

message = greet("Alice")  # Call
print(message)            # Output: Hello, Alice!
Types of Functions
Type	Description	Example
Built-in	Predefined in Python	print(), len(), max()
User-defined	Created by developer	def calculate_tax(income): ...
Lambda	Anonymous one-line function	lambda x: x * 2
Recursive	Calls itself	Factorial, Fibonacci

✅ Best Practices
Use descriptive names → calculate_tax() not func1().

Follow SRP (Single Responsibility Principle).

Document with docstrings:

python
Copy
Edit
def add(a, b):
    """Return the sum of two numbers."""
    return a + b
2. Modules in Python
A module is a single .py file containing reusable code.

Creating a Module
math_utils.py

python
Copy
Edit
def square(x):
    return x ** 2
main.py

python
Copy
Edit
import math_utils
print(math_utils.square(5))   # 25
Importing Options
Method	Example	Use Case
import module	import math	General use
from module import func	from math import sqrt	Specific functions
import module as alias	import pandas as pd	Short name
from module import *	from math import *	🚫 Avoid (namespace pollution)

Special Variable
python
Copy
Edit
if __name__ == "__main__":
    print("Running directly!")
3. Libraries (Packages)
A library is a collection of modules (folder with __init__.py).

Installing
bash
Copy
Edit
pip install numpy pandas
Popular Libraries
Library	Purpose	Example
NumPy	Numerical computing	np.array([1, 2, 3])
Pandas	Data manipulation	pd.read_csv("file.csv")
Matplotlib	Data visualization	plt.plot(x, y)
Requests	HTTP requests	requests.get(url)

4. Built-in Functions
Python has predefined functions available everywhere.

Common Built-ins
python
Copy
Edit
print("Hello")      # Output text
len([1,2,3])        # 3
range(5)            # 0,1,2,3,4
input("Name? ")     # User input
type(10)            # <class 'int'>
Advanced Built-ins
python
Copy
Edit
# map → applies a function
print(list(map(str.upper, ["a", "b"])))   # ['A', 'B']

# filter → keeps condition true
print(list(filter(lambda x: x > 0, [-1, 2, -3])))  # [2]

# zip → combine iterables
print(list(zip([1,2], ["a","b"])))   # [(1, 'a'), (2, 'b')]
5. Functions, Methods, and Classes
Functions
Standalone blocks of code.

python
Copy
Edit
print(len("hello"))  # Built-in function
Methods
Functions belonging to objects (from classes).

python
Copy
Edit
text = "hello"
print(text.upper())  # Method from str class
Classes
Blueprints to create objects.

python
Copy
Edit
class Dog:
    def bark(self):
        return "Woof!"

d = Dog()      # Object
print(d.bark()) # Method
Objects
Instances of classes:

"hi" → instance of str

[1,2,3] → instance of list

6. Data Types & Methods Quick Reference
Data Type	Common Methods
str	.upper(), .lower(), .replace(), .split(), .strip()
list	.append(), .sort(), .pop(), .remove(), .reverse()
dict	.keys(), .values(), .items(), .get(), .update()
int	.bit_length(), .to_bytes() (⚠️ no .upper() here)

7. Example Bringing It Together
python
Copy
Edit
data = [10, 20, 30]
print(len(data))      # Function → 3
data.append(40)       # Method of list
print(data)           # [10, 20, 30, 40]

text = "python"
print(type(text))     # Class → <class 'str'>
print(text.upper())   # Method → 'PYTHON'
✅ Final Takeaways
Function → A block of code (print(), len(), def add()).

Method → A function that belongs to an object (str.upper(), list.sort()).

Class → A blueprint (str, list, dict).

Object → An instance of a class ("hello", [1,2,3]).

Built-ins → Predefined functions available everywhere.

[⬅ Back to Main README](../README.md)