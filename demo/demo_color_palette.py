from plotkit.palettes import qualitative_palette
from plotkit.themes import set_theme
from plotkit.preview import show_palette
from plotkit.utils import save_palette

palette = qualitative_palette(6)

show_palette(palette)
save_palette(palette, "my_default")

set_theme("light")

# apply in matplotlib
import matplotlib.pyplot as plt

plt.bar(range(6), range(6), color=palette)
plt.show()
plt.savefig("color_palette.png")
plt.close()
