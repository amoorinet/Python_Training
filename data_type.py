"""Visualizes Python data types using matplotlib."""
# python_data_type
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, ax = plt.subplots(figsize=(13, 8))
plt.title("Python Data Types", fontsize=16, weight="bold")

# Boxes (x, y, w, h, text, color)
boxes = [
    # No Value
    (0.05, 0.75, 0.2, 0.12, "No Value", "#a6cee3"),
    (0.1, 0.55, 0.1, 0.08, "NoneType\nNone", "#ffffff"),

    # Single Value
    (0.35, 0.75, 0.3, 0.12, "Single Value", "#a6cee3"),
    (0.37, 0.6, 0.1, 0.08, "Numeric", "#b2df8a"),
    (0.37, 0.45, 0.08, 0.06, "int\n15", "#ffffff"),
    (0.47, 0.45, 0.08, 0.06, "float\n3.15", "#ffffff"),
    (0.57, 0.45, 0.1, 0.06, "complex\n3+5j", "#ffffff"),

    (0.5, 0.6, 0.1, 0.08, "str\n'Hello'", "#ffffff"),
    (0.63, 0.6, 0.1, 0.08, "bool\nTrue/False", "#ffffff"),

    (0.77, 0.6, 0.12, 0.08, "Date & Time", "#b2df8a"),
    (0.75, 0.45, 0.1, 0.06, "date\n2026-12-25", "#ffffff"),
    (0.87, 0.45, 0.1, 0.06, "time\n18:05:30", "#ffffff"),
    (0.81, 0.32, 0.14, 0.06, "datetime\n2026-12-25\n18:05:30", "#ffffff"),

    # Multi-Value
    (0.25, 0.25, 0.25, 0.12, "Multi-Values", "#a6cee3"),
    (0.27, 0.1, 0.1, 0.07, "list\n[1,2,3]", "#ffffff"),
    (0.39, 0.1, 0.1, 0.07, "tuple\n(1,2,3)", "#ffffff"),
    (0.51, 0.1, 0.1, 0.07, "set\n{1,2,3}", "#ffffff"),
    (0.63, 0.1, 0.12, 0.07, "dict\n{'a':1}", "#ffffff"),
    (0.77, 0.1, 0.15, 0.07, "array\narray('i',[10,20])", "#ffffff"),
]

# Draw boxes
for (x, y, w, h, text, color) in boxes:
    ax.add_patch(mpatches.Rectangle(
        (x, y), w, h, edgecolor="black", facecolor=color))
    ax.text(x + w/2, y + h/2, text, ha="center",
            va="center", fontsize=10, weight="bold")

# Arrows: No Value
ax.annotate("", xy=(0.15, 0.75), xytext=(0.15, 0.63),
            arrowprops=dict(arrowstyle="->", lw=2))

# Arrows: Single Value → subcategories
ax.annotate("", xy=(0.42, 0.75), xytext=(0.42, 0.68),
            arrowprops=dict(arrowstyle="->", lw=2))
ax.annotate("", xy=(0.55, 0.75), xytext=(0.55, 0.68),
            arrowprops=dict(arrowstyle="->", lw=2))
ax.annotate("", xy=(0.68, 0.75), xytext=(0.68, 0.68),
            arrowprops=dict(arrowstyle="->", lw=2))

# Arrows: Numeric → int/float/complex
ax.annotate("", xy=(0.41, 0.6), xytext=(0.41, 0.51),
            arrowprops=dict(arrowstyle="->", lw=1.5))
ax.annotate("", xy=(0.51, 0.6), xytext=(0.51, 0.51),
            arrowprops=dict(arrowstyle="->", lw=1.5))
ax.annotate("", xy=(0.61, 0.6), xytext=(0.61, 0.51),
            arrowprops=dict(arrowstyle="->", lw=1.5))

# Arrows: Date & Time → children
ax.annotate("", xy=(0.83, 0.6), xytext=(0.8, 0.51),
            arrowprops=dict(arrowstyle="->", lw=1.5))
ax.annotate("", xy=(0.83, 0.6), xytext=(0.9, 0.51),
            arrowprops=dict(arrowstyle="->", lw=1.5))
ax.annotate("", xy=(0.83, 0.6), xytext=(0.88, 0.38),
            arrowprops=dict(arrowstyle="->", lw=1.5))

# Arrows: Multi-Values → children
ax.annotate("", xy=(0.37, 0.25), xytext=(0.32, 0.17),
            arrowprops=dict(arrowstyle="->", lw=2))
ax.annotate("", xy=(0.42, 0.25), xytext=(0.44, 0.17),
            arrowprops=dict(arrowstyle="->", lw=2))
ax.annotate("", xy=(0.47, 0.25), xytext=(0.56, 0.17),
            arrowprops=dict(arrowstyle="->", lw=2))
ax.annotate("", xy=(0.52, 0.25), xytext=(0.69, 0.17),
            arrowprops=dict(arrowstyle="->", lw=2))
ax.annotate("", xy=(0.55, 0.25), xytext=(0.85, 0.17),
            arrowprops=dict(arrowstyle="->", lw=2))

# Hide axes
ax.axis("off")
plt.show()
