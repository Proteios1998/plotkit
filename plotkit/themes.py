import matplotlib.pyplot as plt
import seaborn as sns

def set_theme(theme="light", grid=True, font_scale=1.2):
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
