from plotkit.auto import apply_auto_theme
from plotkit.plots import manhattan_plot, qq_plot
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
plt.savefig("scatter_demo.png", dpi=300)
plt.close()

# Simulated GWAS data
n = 100000
chrom = np.random.randint(1, 23, n)
pos = np.random.randint(1, 1_000_000, n)
pval = np.random.uniform(0, 1, n)

# Apply GWAS theme
apply_auto_theme("gwas")

# Manhattan
ax = manhattan_plot(chrom, pos, pval)
ax.figure.savefig("manhattan_demo.png", dpi=300)

# QQ
ax2 = qq_plot(pval)
ax2.figure.savefig("qq_demo.png", dpi=300)