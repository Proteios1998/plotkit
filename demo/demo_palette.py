from plotkit.palettes import sequential_palette, PALETTES
from plotkit.preview import show_palette, palette_showcase_figure
from plotkit.utils import save_palette
import matplotlib.pyplot as plt
import sys

# Demo of showing the color bar of palette
palette = sequential_palette(6)

show_palette(palette)
save_palette(palette, "my_default")

plt.savefig("colorbar_demo.png", dpi=300)
plt.close()

# Demo of showing the color palette figure
if len(sys.argv)>1 :
    # palette = PALETTES["grgstyle"]
    palette = PALETTES[sys.argv[1]]
else:
    palette = PALETTES["pinkpurple"]
    # palette = [
    # "#FBB463", "#A3B1B3", "#B19BA9", "#EC8780",
    # "#C4B1CB", "#E0DDC4", "#DBECB9", "#8DD1C6"
    # ]
palette_showcase_figure(palette)