[⬅ Back to Main README](../README.md)

# Python String Basics — Deep Guide

## 1) `str(x)` — Convert to String
**What**: Returns the string representation of `x`.

**Details**:
- Non-destructive (doesn't change `x`)
- For numbers, booleans, etc., it's how you safely concatenate with text

**Examples**:
```python
str(42)           # '42'
"age: " + str(30) # 'age: 30'
str(True)         # 'True'
2) type(x) — Show Data Type
What: Returns the class of x.

Use: Quick checks while learning/debugging.

Examples:


type("Aamir")    # <class 'str'>
type(30)         # <class 'int'>
type(3.14)       # <class 'float'>
3) f-strings — String Interpolation
What: Embed expressions inside {} in a string prefixed with f.

Details:

Any expression works: math, function calls, formatting with :

Preferred over "{} {}".format(...) and concatenation

Examples:


name, age = "Aamir", 30
f"Your name is {name} and your age is {age}"  # 'Your name is Aamir...'

price = 9234.235
f"{price:.2f} AED"  # '9234.24 AED'
4) len(s) — Length of String
What: Number of code points (characters) in s.

Details:

Counts spaces and symbols too

Emojis/combined characters can be tricky, but fine for normal text

Examples:


len("123a")          # 4
len("Aamir Ahmed")   # 11 (includes space)
5) s.count(sub[, start[, end]])
What: Non-overlapping count of sub in s.

Details:

Optional start, end slice the region checked

No overlaps: "aaaa".count("aa") == 2, not 3

Examples:


text = "python is easy. python is powerful."
text.count("python")  # 2
"aaaa".count("aa")    # 2
6) s.replace(old, new[, count])
What: Return a copy with old replaced by new.

Details:

If count is given, replace at most count occurrences

Chain it for multiple cleanups

Examples:


"9234,235".replace(",", ".")                # '9234.235'
"$1,9234.235".replace("$","").replace(",","") # '19234.235'
"aaa".replace("a","b", 2)                   # 'bba'
7) Concatenation (+) & Repetition (*)
What: + combines strings; * repeats.

Details:

There is no concat() method for Python str

For many pieces, " ".join(list) is faster/cleaner than many +

Examples:


"Hello, " + "world!"        # 'Hello, world!'
"Aamir " * 3                # 'Aamir Aamir Aamir'
" ".join(["Aamir", "Ahmed"]) # 'Aamir Ahmed'
8) s.split(sep=None, maxsplit=-1) / s.rsplit(...)
What: Split into a list on sep (or any whitespace if sep=None).

Details:

maxsplit limits how many splits

rsplit splits from the right (useful for file paths, "last piece")

Examples:


"Aamir-Sudan-30".split("-")           # ['Aamir', 'Sudan', '30']
"  a  b   c ".split()                 # ['a','b','c'] (any whitespace)
"one,two,three".split(",", 1)         # ['one', 'two,three']
"file.name.ext".rsplit(".", 1)        # ['file.name', 'ext']
9) Indexing & Slicing: s[i], s[a:b:c]
What: Access characters and ranges.

Details:

s[0] first; s[-1] last

Slice is [start:stop:step], stop is exclusive

Strings are immutable (slices return new strings)

Examples:


s = "AAMIR"
s[0]           # 'A'
s[-1]          # 'R'
s[0:4]         # 'AAMI'
"abcdef"[::2]  # 'ace'
"abcdef"[1::2] # 'bdf'
10) s.strip([chars]), lstrip, rstrip
What: Remove leading/trailing chars (default = whitespace).

Details:

With chars, it removes any of those characters until a different char

For exact prefixes/suffixes, prefer removeprefix/removesuffix (Py3.9+)

Examples:


"   Aamir Ahmed   ".strip()         # 'Aamir Ahmed'
"######1974******".strip("#*")      # '1974'
"xxHELLOxx".lstrip("x")             # 'HELLOxx'
"xxHELLOxx".removeprefix("xx")      # 'HELLOxx' (exact token)
11) s.lower() / s.upper() (and s.casefold() for aggressive lower)
What: Change case.

Details:

lower/upper are locale-neutral; casefold() is stronger for comparisons

Examples:


"Email".lower().strip() == "email ".lower().strip()  # True
"ß".lower()       # 'ß'
"ß".casefold()    # 'ss' (better for equality checks)
12) s.startswith(prefix[, start[, end]]) / s.endswith(suffix[, ...])
What: Check beginning/end.

Details:

prefix/suffix can be a tuple to check multiple options

Optional start, end limit to a slice

Examples:


"1998-May-16".startswith("1998")           # True
"file.tar.gz".endswith((".gz", ".zip"))    # True
"abcde".startswith("b", 1)                 # True (slice from index 1)
13) Membership: sub in s
What: True if sub appears in s.

Examples:


"@" in "aamir.ahmed@example.com"   # True
"cat" in "scatter"                 # True
14) s.find(sub[, start[, end]]) / s.rfind(...)
What: Return index of first (or last, for rfind) occurrence; -1 if not found.

Details:

s.index(sub) is similar but raises ValueError if not found

Examples:


"abc-xyz".find("-")        # 3
"abc-xyz".find("/", 0, 3)  # -1
"abc-xyz-123".rfind("-")   # 7
15) s.isalpha() / s.isdigit() / s.isalnum()
What: Character-class checks (Unicode-aware).

Details:

isalpha: letters only

isdigit: digits 0–9 and some other digit chars

isalnum: letters or digits (no spaces/punct)

Examples:


"Maria".isalpha()     # True
"12345".isdigit()     # True
"123٤٥".isdigit()     # True (Arabic-Indic digits)
"User27".isalnum()    # True
"User 27".isalnum()   # False (space)
16) s.isnumeric()
What: Numeric characters (includes digits, vulgar fractions, Roman numerals).

Details: Broader than isdigit.

Examples:


"Ⅻ".isnumeric()    # True (Roman 12)
"²".isnumeric()     # True (superscript two)
"123".isnumeric()   # True
17) s.isspace()
What: String contains only whitespace (and at least one char).

Examples:


"   \t\n".isspace()   # True
"".isspace()          # False (empty string)
18) s.islower() / s.isupper()
What: All cased characters are lower/upper and there's at least one cased char.

Details: Strings with no letters return False for both.

Examples:


"hello".islower()     # True
"HELLO".isupper()     # True
"123!".islower()      # False (no cased letters)
"hello123".isupper()  # False
19) Extra: Common Cleaning Patterns
Phone Normalization with Chained Replace

phone = "+49 (176) 123-4567"
clean = (phone.replace("+","00")
              .replace(" ", "")
              .replace("(", "")
              .replace(")", "")
              .replace("-", ""))
# '00491761234567'
Slicing After Find

tel = "+49-789-12345"
rest_after_first_dash = tel[tel.find("-")+1:]   # '789-12345'
Path Building (Windows)

folder = r"C:\python\bara"
file = "script.py"
path = folder + "\\" + file               # OK

# Better:
import os
os.path.join(folder, file)                # platform-safe
20) Quick "When to Use What"
Use Case	Recommended Method
Interpolate values	f"...{expr}..."
Convert to text	str(x)
Count/locate	count, find/rfind
Replace/clean	replace, strip/lstrip/rstrip, lower/upper/casefold
Split & glue	split/rsplit, "sep".join(list)
Validate characters	isalpha/isdigit/isalnum/isnumeric/isspace
Check patterns	startswith/endswith, 'sub' in s
Pick pieces	indexing s[i], slicing s[a:b:c]