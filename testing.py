"""Str() and type():
1- f use for string interpolation
2- str() convert any data type to string
3- type() returns the data type of an object
4- len() returns the length of an object including all characters,numbers,special characters,
number,strings or whitespace
5- count() returns the number of occurrences of a substring in a string
6- replace() replaces all occurrences of a substring with another substring
7- concat() concatenates two or more strings
8- f strings are used to format strings by embedding expressions inside string literals, using 
curly braces {}
9-split() splits a string into a list of substrings based on a delimiter
10- Extracting using indexing
11- strip() removes leading and trailing whitespace from a string
12- lower() converts a string to lowercase
13- upper() converts a string to uppercase 
14- startswith() checks if a string starts with a specified substring and returns a boolean
15- endswith() checks if a string ends with a specified substring and returns a boolean
16- in operator checks if a substring exists within a string and returns a boolean
17- find() returns the lowest index of a substring if found in the string, otherwise -1
18- isalpha() checks if all characters in a string are alphabetic and returns a boolean
19- isdigit() checks if all characters in a string are digits and returns a boolean
20- isalnum() checks if all characters in a string are alphanumeric (letters and numbers)
and returns a boolean
21- isnumeric() checks if all characters in a string are numeric and returns a boolean
22- isspace() checks if all characters in a string are whitespace and returns a boolean
23- islower() checks if all characters in a string are lowercase and returns a boolean
24- isupper() checks if all characters in a string are uppercase and returns a boolean
 """

NAME = "Aamir Ahmed"
AGE = 30
print(type(NAME))
print(type(AGE))

print(f"your name is {NAME} and your age is {AGE}")
print(5+AGE)
# TypeError: can only concatenate str (not "int") to str
# print("your age is " + (AGE))
# To fix this, we need to convert AGE to a string
print("your age is " + str(AGE))
# still data type of AGE is <class 'int'> unless you convert it as below
AGE = str(AGE)
print(type(AGE))
# print(5+AGE)
# TypeError: can only concatenate str (not "int") to str
PASSWORD = "123a"
print(len(PASSWORD))

PYTHON = """python is easy to learn
python is powerful
python is versatile
python is dynamic
many people like
"""
print(PYTHON.count("python"))
PRICE = "9234,235"
PRICE = PRICE.replace(",", ".")
print(f"{float(PRICE)} AED")
# neste replace
PRICE_2 = "$1,9234.235"
print(PRICE_2.replace("$", "").replace(",", ""))
# convert the Phone number to only digit +49 (176) 123-4567
PHONE = "+49 (176) 123-4567"
print(PHONE.replace("+", "00").replace(" ",
      "").replace("(", "").replace(")", "").replace("-", ""))
FIRST_NAME = "Aamir"
LAST_NAME = "Ahmed"
# FULL_NAME = FIRST_NAME, LAST_NAME)
FULL_NAME = FIRST_NAME + " " + LAST_NAME
print(f"your name is {FULL_NAME} and your age is {AGE}")
FOLDER = "C:\\python\\bara"
FILE = "script.py"
FILE_PATH = FOLDER + "\\" + FILE
print(FILE_PATH)
# power of f strings
print(f"my name is {FULL_NAME} and my age is {AGE}")
print("my name is" + " " + FIRST_NAME + " " +
      LAST_NAME + " and my age is " + str(AGE))
AAMIR_DATA = "Aamir-Sudan-30"
AAMIR_LIST = AAMIR_DATA.split("-")
print(AAMIR_LIST)
# string repetition
print(f" {AAMIR_LIST[0] * 3}")
print("Aamir " * 3)
print("#"*20)
# indexing in python and slicing
# from left to right start by 0
# from right to left start by -1
# indexing allows you to access individual elements of a
# sequence (like a string or a list) using their position
print(AAMIR_LIST[0])  # prints "Aamir"
print(AAMIR_LIST[1])  # prints "Sudan"
print(AAMIR_LIST[2])  # prints "30"
MY_NAME = "AAMIR"
print(MY_NAME[0])  # prints "A"
print(MY_NAME[-1])  # prints "R"
print(MY_NAME[0:4:1])  # prints "AAMI"
# Clean White Spaces
# leading and trailing whitespace
NAME_WITH_SPACES = "   Aamir Ahmed   "
print(NAME_WITH_SPACES.strip())
# leading whitespace
print(NAME_WITH_SPACES.lstrip())
# trailing whitespace
print(NAME_WITH_SPACES.rstrip())
REX = "######1974******".strip("#").strip("*")
print(REX)
# Example
DATA = "   Data Engineering IS THE BEST SEINCE IN FUTURE    "
CHAR_IN_DATA = len(DATA)
SPACING_NO = len(DATA.strip())
NO_OF_SPACES = CHAR_IN_DATA - SPACING_NO
IS_CLEAN = CHAR_IN_DATA == SPACING_NO
print("is my data clean:", IS_CLEAN)
if IS_CLEAN:
    print("my data is clean")
else:
    print("my data is not clean")

####################################
NAME_MIX = "AAMIR Ahmed moHmmed ahmeD"
# print(MY_NAME[include:not include index:step])
# step 1 means take every character
print(NAME_MIX.lower())
print(NAME_MIX.upper())
# using lower() for cleaning data
SEARCH = " Email".lower().strip()
DATA_3 = "email ".lower().strip()
print(SEARCH == DATA_3)
BAD_DATA = "968-Maria, (D@t@ Engineer ) ;; 27y"
# test need output as name: Maria | rule: data Engineer | Age: 27
DOB = "1998-May-16"
print(DOB.startswith("1998"))
print(DOB.endswith("16"))
TEL1 = "+49-176-12345"
TEL2 = "+49-789-12345"
if TEL1.startswith("+49"):
    print("this is a german number")
else:
    print("this is not a german number")
MY_EMAIL = "aamir.ahmed@example.com"
if "@" in MY_EMAIL: # other way for seaching or validation
    print("this is a valid email")
else:
    print("this is not a valid email")
print(TEL2[int(TEL2.find("-"))+1:]) # slicing after finding the index of
# <class 'str'>
# <class 'int'>
# your name is Aamir Ahmed and your age is 30
# 35
# your age is 30
# <class 'str'>
# 9234.235 AED
# 19234.235
# 00491761234567
# your name is Aamir Ahmed and your age is 30
# C:\python\bara\script.py
