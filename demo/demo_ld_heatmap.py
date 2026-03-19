import plotkit as pk
from plotkit.plots import ld_heatmap
import numpy as np
import matplotlib.pyplot as plt

# Simulate LD matrix
n = 60
X = np.random.randn(n, n)
ld = np.corrcoef(X)

pk.auto.apply_auto_theme("ld_heatmap")

ax = ld_heatmap(ld, title="LD Heatmap (Simulated)")

plt.savefig("ld_heatmap_demo.png", dpi=300)
plt.close()
