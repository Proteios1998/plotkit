from plotkit.palettes import sequential_palette
from plotkit.themes import set_theme
from plotkit.preview import show_palette
from plotkit.utils import save_palette

palette = sequential_palette(6)

show_palette(palette)
save_palette(palette, "my_default")

set_theme("light")


# apply in matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

sns.palplot(palette)
plt.savefig("colorbar_demo.png", dpi=300)
plt.close()
