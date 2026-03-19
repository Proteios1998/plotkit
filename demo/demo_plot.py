from plotkit.auto import apply_auto_theme
import matplotlib.pyplot as plt
import numpy as np
from plotkit.palettes import PALETTES

# Automatically configure everything
palette = apply_auto_theme("scatter", n_colors=1, font="Nimbus Sans")
print(palette)

x = np.random.randn(100)
y = np.random.randn(100)

plt.scatter(x, y, color=PALETTES["grgstyle"][1])
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Auto-themed Scatter Plot")
plt.savefig("test_scatter.png", dpi=300)
plt.close()