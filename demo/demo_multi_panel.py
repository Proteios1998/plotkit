import plotkit as pk
import numpy as np
import matplotlib.pyplot as plt

pk.auto.apply_auto_theme("scatter")

fig, axes = pk.themes.setup_multi_panel(2, 2, figsize=(10,10))

x = np.random.randn(200)
axes[0].scatter(x, np.random.randn(200))
axes[0].set_title("Panel A")
axes[1].hist(x, bins=20)
axes[1].set_title("Panel B")
axes[2].scatter(x, np.random.randn(200))
axes[2].set_title("Panel C")
axes[3].hist(x, bins=20)
axes[3].set_title("Panel D")

pk.themes.add_panel_labels(fig, axes)

fig.tight_layout()
plt.savefig("multi_panel_demo.png", dpi=300)
