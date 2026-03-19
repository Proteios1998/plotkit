import matplotlib.pyplot as plt
import seaborn as sns

def set_theme(theme="minimal", grid=False, font_scale=1.2):
    if theme == "light":
        sns.set_style("whitegrid" if grid else "white")
    elif theme == "dark":
        sns.set_style("darkgrid" if grid else "dark")
    elif theme == "minimal":
        sns.set_style("ticks")

    sns.set_context("notebook", font_scale=font_scale)

    plt.rcParams.update({
        "figure.figsize": (6, 4),
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.titleweight": "bold",
        "axes.labelsize": 12,
        "legend.frameon": False,
    })

def set_font(font_family="Nimbus Sans"):
    """
    Set publication-friendly sans-serif fonts.
    Falls back gracefully if not installed.
    """

    font_list = [
        font_family,
        "Nimbus Sans",
        "Liberation Sans",
        "DejaVu Sans"
    ]
    
    plt.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": font_list,
        "axes.unicode_minus": False,
    })

    # important for PDF/illustrator compatibility
    plt.rcParams["pdf.fonttype"] = 42
    plt.rcParams["ps.fonttype"] = 42

def auto_fontsize(fig=None, base=10):
    """
    Automatically scale font sizes based on figure size.
    """

    if fig is None:
        fig = plt.gcf()

    width, height = fig.get_size_inches()
    scale = (width * height) ** 0.5 / 5  # normalize around 5x5 figure

    sizes = {
        "title": base * 2 * scale,
        "label": base * 1.4 * scale,
        "ticks": base * scale,
        "legend": base * scale,
    }

    plt.rcParams.update({
        "axes.titlesize": sizes["title"],
        "axes.labelsize": sizes["label"],
        "xtick.labelsize": sizes["ticks"],
        "ytick.labelsize": sizes["ticks"],
        "legend.fontsize": sizes["legend"],
    })

    return sizes

def set_theme_preset(name="paper"):
    if name == "paper":
        sns.set_style("white")
        plt.rcParams.update({
            "figure.figsize": (6, 4),
            "axes.linewidth": 1,
            "axes.labelsize": 12,
            "axes.titlesize": 14,
            "xtick.labelsize": 10,
            "ytick.labelsize": 10,
        })

    elif name == "presentation":
        sns.set_style("whitegrid")
        plt.rcParams.update({
            "figure.figsize": (8, 5),
            "axes.labelsize": 14,
            "axes.titlesize": 16,
        })

    elif name == "minimal":
        sns.set_style("ticks")
        plt.rcParams.update({
            "axes.spines.top": False,
            "axes.spines.right": False,
        })

import matplotlib.pyplot as plt

def setup_multi_panel(
    nrows,
    ncols,
    figsize=(8, 6),
    font_scale=1.0,
    sharex=False,
    sharey=False
):
    """
    Create a multi-panel figure with consistent styling.
    """

    fig, axes = plt.subplots(
        nrows,
        ncols,
        figsize=figsize,
        sharex=sharex,
        sharey=sharey
    )

    # Flatten axes for easy iteration
    if hasattr(axes, "flatten"):
        axes = axes.flatten()
    else:
        axes = [axes]

    # Apply global font scaling
    _apply_figure_fontsize(fig, font_scale)

    return fig, axes