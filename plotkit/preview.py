import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def show_palette(palette):
    fig, ax = plt.subplots(figsize=(len(palette), 1))
    for i, color in enumerate(palette):
        ax.add_patch(plt.Rectangle((i, 0), 1, 1, color=color))

    ax.set_xlim(0, len(palette))
    ax.set_ylim(0, 1)
    ax.axis("off")
    plt.show()

def palette_showcase_figure(
    palette,
    scatter_df=None,
    violin_df=None,
    bar_df=None,
    radial_df=None,
    n=300,
    seed=0,
    figsize=(8, 10)
):
    """
    Multi-panel palette showcase figure with optional internal data simulation.

    If datasets are not provided, they will be simulated automatically.

    Parameters
    ----------
    palette : list of hex colors
    scatter_df : DataFrame [x, y, group]
    violin_df  : DataFrame [sample, value]
    bar_df     : DataFrame [x, category]
    radial_df  : DataFrame [label, value]
    n : number of samples for simulation
    seed : random seed
    """

    np.random.seed(seed)
    sns.set_style("ticks", {
        'axes.facecolor': '#E0E0E0',  # Light Grey Background
        'axes.edgecolor': '#505050',  # Dark Grey Border
        'axes.linewidth': 1.5,       # Thicker border
        'xtick.color': '#505050',    # Grey ticks
        'ytick.color': '#505050'
    })
    
    from plotkit.themes import set_font, auto_fontsize
    set_font()

    n_colors = len(palette)
    group_labels = [chr(65 + i) for i in range(n_colors)]  # A, B, C...

    # ----------------------
    # (1) Simulate data if not provided
    # ----------------------
    if scatter_df is None:
        scatter_df = pd.DataFrame({
            "x": np.random.randn(n),
            "y": np.random.randn(n),
            "group": np.random.choice(group_labels, n)
        })

    if violin_df is None:
        assert n_colors >= 4, "At least 4 colors are required for violin plot"
        violin_df = pd.DataFrame({
            "sample": np.random.choice(
                [f"Sample {i+1}" for i in range(min(4, n_colors))], n
            ),
            "value": np.random.randn(n) * 10 + 50
        })

    if bar_df is None:
        bar_df = pd.DataFrame({
            "x": np.random.choice(
                ["Fair", "Good", "Ideal", "Premium", "Very Good"], n
            ),
            "category": np.random.choice(group_labels, n)
        })

    if radial_df is None:
        radial_df = pd.DataFrame({
            "label": [f"A{i+1}" for i in range(n_colors)],
            "value": np.random.rand(n_colors) + 0.5
        })

    # ----------------------
    # Layout
    # ----------------------
    fig = plt.figure(figsize=figsize)
    gs = fig.add_gridspec(3, 2, height_ratios=[1, 1, 0.25])
    # ----------------------
    # (2) Scatter
    # ----------------------
    ax1 = fig.add_subplot(gs[0, 0])
    sns.scatterplot(
        data=scatter_df,
        x="x", y="y",
        hue="group",
        palette=palette,
        s=30, alpha=0.8,
        ax=ax1,
        legend=False
    )
    ax1.set_title("Scatter")

    # ----------------------
    # (3) Violin
    # ----------------------
    ax2 = fig.add_subplot(gs[0, 1])
    sns.violinplot(
        data=violin_df,
        x="sample", y="value",
        palette=palette,
        ax=ax2
    )
    sns.boxplot(
        data=violin_df,
        x="sample", y="value",
        width=0.15,
        color="white",
        ax=ax2
    )
    ax2.set_title("Violin")

    # ----------------------
    # (4) Radial
    # ----------------------
    ax3 = fig.add_subplot(gs[1, 0], projection='polar')

    angles = np.linspace(0, 2*np.pi, len(radial_df), endpoint=False)
    values = radial_df["value"].values

    ax3.bar(
        angles,
        values,
        color=palette[:len(values)],
        alpha=0.8
    )

    # ax3.set_xticks(angles)
    ax3.set_xticklabels(radial_df["label"])
    ax3.set_yticks([])
    ax3.spines['polar'].set_visible(False)
    ax3.set_title("Radial")
    
    # ----------------------
    # (5) Stacked bar
    # ----------------------
    ax4 = fig.add_subplot(gs[1, 1])

    bar_pivot = (
        bar_df
        .groupby(["x", "category"])
        .size()
        .unstack(fill_value=0)
    )

    bar_pivot = bar_pivot.div(bar_pivot.sum(axis=1), axis=0)

    bottom = np.zeros(len(bar_pivot))
    for i, col in enumerate(bar_pivot.columns):
        ax4.bar(
            bar_pivot.index,
            bar_pivot[col],
            bottom=bottom,
            color=palette[i % len(palette)]
        )
        bottom += bar_pivot[col].values

    ax4.set_title("Stacked Bar")

    # ----------------------
    # (6) Palette strip
    # ----------------------
    ax5 = fig.add_subplot(gs[2, :])

    for i, color in enumerate(palette):
        ax5.add_patch(plt.Rectangle((i, 0), 1, 1, color=color, ec=(0,0,0,0)))

    ax5.set_xlim(0, len(palette))
    ax5.set_ylim(0, 1)
    ax5.set_xticks(np.arange(len(palette)) + 0.5)
    ax5.set_xticklabels(palette, rotation=45)
    ax5.set_yticks([])
    ax5.set_title("Palette")

    # ----------------------
    # Styling
    # ----------------------
    def lighten_color(hex_color, amount=0.85):
        """
        Lighten a hex color by mixing with white.

        amount: 0 → original color
                1 → white
        """
        import matplotlib.colors as mc

        c = np.array(mc.to_rgb(hex_color))
        white = np.array([1, 1, 1])
        return mc.to_hex(c + (white - c) * amount)
    bg_color = lighten_color(palette[0], 0.65)
    panel_color = lighten_color(palette[0], 0.92)
    
    for ax in [ax1, ax2, ax3, ax4]:
        ax.set_facecolor(color=panel_color)

    fig.patch.set_facecolor(color=bg_color)

    plt.tight_layout()
    plt.show()
    plt.savefig("palette_demo.png", dpi=300)
