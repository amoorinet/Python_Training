[⬅ Back to Main README](../README.md)
# 📑 Markdown Syntax Cheat Sheet  

## Headings  
```markdown
# H1  
## H2  
### H3  
#### H4  
##### H5  
###### H6  
H1
H2
H3
H4
H5
H6
Text Formatting

*italic* or _italic_  
**bold** or __bold__  
***bold italic***  
~~strikethrough~~  
italic | bold | bold italic | strikethrough

Lists
Unordered (bullets)

- Item 1  
- Item 2  
  - Subitem  
Item 1

Item 2

Subitem

Ordered (numbers)

1. First  
2. Second  
   1. Sub-numbered  
First

Second

Sub-numbered

Links
[Link text](https://example.com)  
[Relative link](docs/file.md)  
Link text
Relative link

Images
![Alt text](path/to/image.png)  
(Images render if the file exists in your repo.)

Code
Inline code:
Use `print("hello")` in Python.  
Use print("hello") in Python.

Block code (fenced):

```python
def greet(name):
    return f"Hello {name}"

```python
def greet(name):
    return f"Hello {name}"
Blockquotes

> This is a blockquote.  
>> Nested blockquote.  
This is a blockquote.

Nested blockquote.

Tables

| Name   | Age | Country |  
|--------|-----|---------|  
| Aamir  | 30  | UAE     |  
| Maria  | 28  | Sudan   |  
Name	Age	Country
Aamir	30	UAE
Maria	28	Sudan

Horizontal Line

---
Task Lists (Checkboxes)

- [x] Done  
- [ ] To do  
 Done

 To do

Notes / Alerts (GitHub flavored)

> 💡 Tip: Use `.gitignore` to avoid pushing venv files.  
> ⚠️ Warning: Don’t commit secrets like API keys.  
💡 Tip: Use .gitignore to avoid pushing venv files.
⚠️ Warning: Don’t commit secrets like API keys.

✅ Keep this handy: With just these, you can document projects professionally on GitHub.


