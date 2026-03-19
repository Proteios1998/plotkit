from plotkit.palettes import palette_showcase_figure, PALETTES
import sys

palette = [
    "#FBB463", "#A3B1B3", "#B19BA9", "#EC8780",
    "#C4B1CB", "#E0DDC4", "#DBECB9", "#8DD1C6"
]

if len(sys.argv)>1 :
    # palette = PALETTES["grgstyle"]
    palette = PALETTES[sys.argv[1]]
palette_showcase_figure(palette)

