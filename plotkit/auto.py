import seaborn as sns
import matplotlib.pyplot as plt
from .palettes import qualitative_palette, sequential_palette, diverging_palette, PALETTES
from .themes import set_font, auto_fontsize
import seaborn as sns
import matplotlib.pyplot as plt
from .palettes import qualitative_palette, sequential_palette, diverging_palette

def apply_auto_theme(plot_type, palette_name=None, n_colors=6, font="Arial", figsize=(6,4)):
    """
    Automatically select theme + palette based on plot type.
    """
    if plot_type == "scatter":
        sns.set_style("ticks")
        if n_colors < len(PALETTES["grgstyle"]):
            palette = PALETTES["grgstyle"][:n_colors]
        else:
            palette = qualitative_palette(n_colors)

    elif plot_type == "line":
        sns.set_style("ticks")
        if n_colors < len(PALETTES["grgstyle"]):
            palette = PALETTES["grgstyle"][:n_colors]
        else:
            palette = qualitative_palette(n_colors)

    elif plot_type == "bar":
        sns.set_style("whitegrid")
        if n_colors < len(PALETTES["grgstyle"]):
            palette = PALETTES["grgstyle"][:n_colors]
        else:
            palette = qualitative_palette(n_colors)

    elif plot_type == "heatmap":
        sns.set_style("white")
        palette = diverging_palette(9)

    elif plot_type == "gwas":
        # Manhattan plot style
        sns.set_style("white")
        palette = ["#757575", "#EFA130"]  # alternating chromosomes

    elif plot_type == "ld_heatmap":
        sns.set_style("white")
        palette = sequential_palette(10, base_color="#2166ac")
        plt.rcParams.update({
            "axes.spines.top": False,
            "axes.spines.right": False,
        })
    elif plot_type == "qq":
        sns.set_style("white")
        palette = ["#7BC0CD"]
    else:
        sns.set_style("whitegrid")
        palette = qualitative_palette(n_colors)

    plt.rcParams["figure.figsize"] = figsize
    # create a dummy fig to scale fonts
    fig = plt.figure(figsize=figsize)
    auto_fontsize(fig)
    plt.close(fig)
    
    sns.set_palette(palette)
    set_font(font)
    return palette

