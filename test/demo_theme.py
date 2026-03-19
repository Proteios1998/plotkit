from plotkit.auto import apply_auto_theme
import matplotlib.pyplot as plt
import numpy as np

# Automatically configure everything
palette = apply_auto_theme("scatter", n_colors=5)

x = np.random.randn(100)
y = np.random.randn(100)

plt.scatter(x, y)
plt.title("Auto-themed Scatter Plot")
plt.show()
