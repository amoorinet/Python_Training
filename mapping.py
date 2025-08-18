# Class_Object_Method
"""Diagrams for Python concepts (Class → Object → Method, Data Types)."""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Create a diagram using matplotlib
fig, ax = plt.subplots(figsize=(10, 6))

# Nodes (rectangles)
ax.add_patch(mpatches.Rectangle((0.05, 0.7), 0.25, 0.15,
             edgecolor="black", facecolor="#a6cee3"))
ax.text(0.175, 0.775, "Class\n(str, list, dict, int)",
        ha="center", va="center", fontsize=11, weight="bold")

ax.add_patch(mpatches.Rectangle((0.4, 0.7), 0.25, 0.15,
             edgecolor="black", facecolor="#b2df8a"))
ax.text(0.525, 0.775,
        "Object\n('hello', [1,2,3], 10)", ha="center", va="center", fontsize=11, weight="bold")

ax.add_patch(mpatches.Rectangle((0.75, 0.7), 0.2, 0.15,
             edgecolor="black", facecolor="#fb9a99"))
ax.text(0.85, 0.775,
        "Method\n(.upper(), .sort())", ha="center", va="center", fontsize=11, weight="bold")

# Functions box (separate to show it works across objects)
ax.add_patch(mpatches.Rectangle((0.35, 0.35), 0.3, 0.15,
             edgecolor="black", facecolor="#fdbf6f"))
ax.text(0.5, 0.425,
        "Functions\n(print(), len(), type())",
        ha="center", va="center", fontsize=11, weight="bold")

# Arrows between Class → Object → Method
ax.annotate("", xy=(0.35, 0.775), xytext=(0.3, 0.775),
            arrowprops=dict(arrowstyle="->", lw=2))
ax.annotate("", xy=(0.7, 0.775), xytext=(0.65, 0.775),
            arrowprops=dict(arrowstyle="->", lw=2))

# Arrow from Function → Object
ax.annotate("", xy=(0.5, 0.7),
            xytext=(0.5, 0.5),
            arrowprops=dict(arrowstyle="->", lw=2, linestyle="dashed")
            )

# Labels for clarity
ax.text(0.32, 0.82, "creates", fontsize=9, ha="center")
ax.text(0.67, 0.82, "has", fontsize=9, ha="center")
ax.text(0.53, 0.61, "applies to", fontsize=9, ha="center")

# Clean up chart
ax.axis("off")
plt.title(
    "Python Relationship: Class → Object → Method (with Functions)", fontsize=14,
    weight="bold")

plt.show()
