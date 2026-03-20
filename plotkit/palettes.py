import numpy as np
import matplotlib.colors as mcolors
import pandas as pd
import matplotlib.pyplot as plt

def generate_palette(n=5, hue_range=(0, 1), saturation=0.65, lightness=0.55):
    """
    Generate evenly spaced colors in HSL space.
    """
    hues = np.linspace(hue_range[0], hue_range[1], n, endpoint=False)
    colors = [mcolors.hsv_to_rgb((h, saturation, lightness)) for h in hues]
    return [mcolors.to_hex(c) for c in colors]


def qualitative_palette(n=8):
    return generate_palette(n, saturation=0.7, lightness=0.6)


def sequential_palette(n=6, base_color="#1f77b4", start_color="#ececec"):
    base = np.array(mcolors.to_rgb(base_color))
    start = np.array(mcolors.to_rgb(start_color))
    colors = [start + (base - start) * i / (n - 1) for i in range(n)]
    return [mcolors.to_hex(c) for c in colors]


def diverging_palette(n=7, low="#d73027", high="#4575b4"):
    low_rgb = np.array(mcolors.to_rgb(low))
    high_rgb = np.array(mcolors.to_rgb(high))

    mid = np.array([1, 1, 1])
    half = n // 2

    colors = []
    for i in range(half):
        t = i / (half - 1)
        colors.append(mcolors.to_hex(low_rgb * (1 - t) + mid * t))

    if n % 2 == 1:
        colors.append("#ffffff")

    for i in range(half):
        t = i / (half - 1)
        colors.append(mcolors.to_hex(mid * (1 - t) + high_rgb * t))

    return colors

PALETTES = {
    # GRG-style (blue and orange)
    "grgstyle": [
        "#51999F","#4198AC", "#7BC0CD", "#BFDFD2",
        "#DBCB92", "#ECB66C", "#EA9E58", "#ED8D5A"],
    
    # Purple/pink-style
    "pinkpurple": [
        "#B6B3D6", "#CFCCE3", "#D5D1D1",
        "#F6DFD6", "#F8B2A2", "#E9687A"
    ],
    
    # Ocean breeze-style
    "oceanbreeze" : [
      "#BFDFD2", "#51999F", "#4198AC", "#7BC0CD",
      "#DBCB92", "#ECB66C", "#EA9E58", "#ED8D5A"  
    ],
    
    # Sea sunset-style (blue and pink)
    "seasunset" : [
        "#FC757B", "#F97F5F", "#FAA26F", "#FDCD94", 
        "#FEE199", "#B0D6A9", "#65BDBA"],
    
    # Light rainbow-style
    "lightrainbow" : [
        "#DB697A", "#EE8575", "#FBB482",
        "#CDEBB8", "#9CD7BC", "#867BB9"],
    
    # Nature-style (clean, not recommend)
    "nature": [
        "#3C5488", "#8491B4", "#4DBBD5", "#00A087",
         "#F39B7F", "#E64B35"
    ],
    
    # Science-style (bold contrast, not recommend)
    "science": [
        "#3B4992", "#631879", "#BB0021", "#EE0000", 
        "#008280", "#008B45", 
    ],

    # Tableau-like
    "tableau": [
        "#4E79A7", "#F28E2B", "#E15759",
        "#76B7B2", "#59A14F", "#EDC948",
        "#B07AA1", "#FF9DA7"
    ],

    # Colorblind-safe
    "colorblind": [
        "#0072B2", "#009E73", "#F0E442",
        "#E69F00", "#CC79A7", "#D55E00"
    ],

    # 🌊 Cool sequential (LD / heatmaps)
    "cool_seq": [
        "#F7FBFF", "#DEEBF7", "#C6DBEF",
        "#9ECAE1", "#6BAED6", "#3182BD", "#08519C"
    ],

    # 🔥 Diverging (for signed effects)
    "diverging_red_blue": [
        "#B2182B", "#EF8A62", "#FDDBC7",
        "#F7F7F7","#D1E5F0", "#67A9CF", "#2166AC"
    ],

    # 🧬 GWAS alternating
    "gwas": ["#8491B4", "#DD8452"],

    # ⚫ Minimal grayscale (papers)
    "grayscale": [
        "#000000", "#444444", "#888888", "#CCCCCC"
    ],
}
